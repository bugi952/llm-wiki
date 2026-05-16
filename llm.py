import json
import logging
import os
import subprocess
import time

from db import increment_api_count

logger = logging.getLogger(__name__)

MAX_RETRIES = 5
RATE_LIMIT_WAIT = 60


def codex_call(prompt, conn=None, timeout=None, expect_json=False, **kwargs):
    """Codex CLI로 LLM 호출. ChatGPT Plus 구독 사용.

    Args:
        prompt: LLM에 보낼 프롬프트 텍스트
        conn: DB connection (API 카운터용, optional)
        timeout: subprocess 타임아웃 (초)
        expect_json: True면 JSON 파싱 검증 후 dict 반환

    Returns:
        str or dict/list (expect_json=True)
    """
    if timeout is None:
        try:
            from config import get_config
            timeout = get_config()["codex"]["cli_timeout"]
        except Exception:
            timeout = 120

    last_error = None

    for attempt in range(MAX_RETRIES):
        try:
            codex_bin = os.path.expanduser("~/.npm-global/bin/codex")
            cmd = [codex_bin, "exec", "--sandbox", "workspace-write", "-"]

            result = subprocess.run(
                cmd,
                input=prompt,
                capture_output=True, text=True, timeout=timeout,
            )

            if result.returncode != 0:
                stderr = result.stderr[:500]
                if "rate" in stderr.lower() or "limit" in stderr.lower():
                    logger.warning("Rate limit hit, waiting %ds (attempt %d/%d)",
                                   RATE_LIMIT_WAIT, attempt + 1, MAX_RETRIES)
                    time.sleep(RATE_LIMIT_WAIT)
                    continue
                raise RuntimeError(f"Codex CLI failed: {stderr}")

            output = result.stdout.strip()

            if expect_json:
                # Try direct parse first
                try:
                    parsed = json.loads(output)
                    if conn:
                        increment_api_count(conn)
                    return parsed
                except json.JSONDecodeError:
                    pass

                # Fallback: extract JSON from mixed output
                arr_start = output.find("[")
                obj_start = output.find("{")

                if expect_json == "array" and arr_start >= 0 and (obj_start < 0 or arr_start < obj_start):
                    end = output.rfind("]")
                    if end > arr_start:
                        parsed = json.loads(output[arr_start:end + 1])
                        if conn:
                            increment_api_count(conn)
                        return parsed

                if obj_start >= 0:
                    depth = 0
                    for i, ch in enumerate(output[obj_start:], obj_start):
                        if ch == "{":
                            depth += 1
                        elif ch == "}":
                            depth -= 1
                            if depth == 0:
                                if conn:
                                    increment_api_count(conn)
                                return json.loads(output[obj_start:i + 1])

                raise json.JSONDecodeError(
                    "No JSON found in output", output[:200], 0)

            # Plain text response
            if conn:
                increment_api_count(conn)
            return output

        except subprocess.TimeoutExpired:
            last_error = f"Codex CLI timed out after {timeout}s"
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

    raise RuntimeError(f"Codex CLI failed after {MAX_RETRIES} retries: {last_error}")


# Backward-compatible alias
claude_call = codex_call
