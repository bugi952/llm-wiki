---
description: "push 전 자동 검수. git push 요청 시 자동 트리거. skip review로 우회 가능"
allowed-tools: Read, Glob, Grep, Bash(git diff*), Bash(git log*), Bash(pytest*), Bash(ruff*), Bash(python -m py_compile*), Bash(git push*)
---

push 전 검수 파이프라인. 모든 단계 통과해야 push 실행.

## Step 1: 시크릿 스캔

staged diff에서 아래 패턴 탐지. 하나라도 발견 -> BLOCK:
- API 키 (sk-ant-, AKIA, FRED_, ECOS_)
- Private key (`-----BEGIN.*PRIVATE KEY-----`)
- 하드코딩된 비밀번호 (`password\s*=\s*['"]`)
- 머지 충돌 마커 (`<<<<<<<`, `=======`, `>>>>>>>`)

```bash
STAGED_DIFF=$(git diff --staged)
echo "$STAGED_DIFF" | grep -nE '(AKIA[0-9A-Z]{16}|-----BEGIN.*PRIVATE KEY-----|password\s*=\s*['\''"]|sk-[a-zA-Z0-9]{20,}|<{7}|={7}|>{7})' && echo 'BLOCKED: 시크릿 또는 머지 충돌 감지' || echo 'PASS: 시크릿 스캔 통과'
```

발견 시: 해당 라인 + 수정 방법 안내 (환경변수 이동, .gitignore 추가 등).

## Step 2: 빌드 확인

변경된 .py 파일에 대해:
```bash
python -m py_compile <changed_file.py>
```

빌드 실패 -> BLOCK.

## Step 3: 린트

```bash
ruff check <changed_files>
```

린트 에러 -> BLOCK. 경고 -> 리포트만.

## Step 4: 코드 리뷰 트리거

`/review-code` 자동 실행 (fork 격리).
- 가중 평균 3.5+ -> PASS
- 가중 평균 3.5- -> FAIL + 수정 사항 반환

## Step 5: 리포트 + Push

```
## Pre-Push Summary
Branch: <current> -> origin
Files: N | Diff: N lines

- 시크릿 스캔:  PASS / BLOCKED
- 빌드:        PASS / FAIL
- 린트:        PASS / FAIL / SKIP
- 코드 리뷰:   PASS (점수) / FAIL

Overall: READY TO PUSH / BLOCKED -- <reason>
```

Overall = READY TO PUSH일 때만 `git push` 실행.
