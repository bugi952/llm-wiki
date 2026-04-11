import json
import logging
import subprocess
import time

from db import increment_api_count

logger = logging.getLogger(__name__)

MAX_RETRIES = 5
RATE_LIMIT_WAIT = 60


def claude_call(prompt, conn=None, timeout=None, expect_json=False):
    """Claude CLI로 LLM 호출. Max 구독 사용, API 키 불필요.

    Args:
        prompt: LLM에 보낼 프롬프트 텍스트
        conn: DB connection (API 카운터용, optional)
        timeout: subprocess 타임아웃 (초)
        expect_json: True면 JSON 파싱 검증 후 dict 반환

    Returns:
        str or dict (expect_json=True)
    """
    if timeout is None:
        try:
            from config import get_config
            timeout = get_config()["claude"]["cli_timeout"]
        except Exception:
            timeout = 120

    last_error = None

    counted = False

    for attempt in range(MAX_RETRIES):
        try:
            if conn and not counted:
                increment_api_count(conn)
                counted = True

            result = subprocess.run(
                ["claude", "-p", prompt, "--model", "haiku"],
                capture_output=True, text=True, timeout=timeout,
            )

            if result.returncode != 0:
                stderr = result.stderr[:500]
                # Rate limit detection
                if "rate" in stderr.lower() or "limit" in stderr.lower():
                    logger.warning("Rate limit hit, waiting %ds (attempt %d/%d)",
                                   RATE_LIMIT_WAIT, attempt + 1, MAX_RETRIES)
                    time.sleep(RATE_LIMIT_WAIT)
                    continue
                raise RuntimeError(f"Claude CLI failed: {stderr}")

            output = result.stdout.strip()

            if expect_json:
                start = output.find("{")
                if start < 0:
                    raise json.JSONDecodeError(
                        "No JSON object found in output",
                        output[:200], 0)
                # Find matching closing brace by counting depth
                depth = 0
                for i, ch in enumerate(output[start:], start):
                    if ch == "{":
                        depth += 1
                    elif ch == "}":
                        depth -= 1
                        if depth == 0:
                            return json.loads(output[start:i + 1])

            return output

        except subprocess.TimeoutExpired:
            last_error = f"Claude CLI timed out after {timeout}s"
            logger.warning("%s (attempt %d/%d)", last_error, attempt + 1, MAX_RETRIES)
        except json.JSONDecodeError as e:
            last_error = f"JSON parse failed: {e}"
            logger.warning("%s (attempt %d/%d)", last_error, attempt + 1, MAX_RETRIES)
        except RuntimeError as e:
            last_error = str(e)
            logger.warning("%s (attempt %d/%d)", last_error, attempt + 1, MAX_RETRIES)

        # Exponential backoff: 1s, 2s, 4s, 8s, 16s
        backoff = 2 ** attempt
        time.sleep(backoff)

    raise RuntimeError(f"Claude CLI failed after {MAX_RETRIES} retries: {last_error}")
