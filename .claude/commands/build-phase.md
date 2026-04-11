---
description: "Phase 진행 상태 확인. 현재 Phase + 다음 할 일 표시"
allowed-tools: Read, Glob, Grep
---

현재 Phase 진행 상태를 확인하고 다음 할 일을 안내한다.

## Phase 정의

!`cat docs/testing.md 2>/dev/null`

## 현재 상태

!`git log --oneline -10 2>/dev/null`

## 체크

1. docs/testing.md에서 현재 Phase의 수락 조건 목록을 읽는다
2. 각 조건의 충족 여부를 코드/테스트 기반으로 확인한다
3. 미충족 항목이 다음 할 일이다

## 보고 형식

```
# Phase N: [Phase 이름]

## 수락 조건
- [x] 조건 1
- [ ] 조건 2 <- 다음 할 일
- [ ] 조건 3

## 다음 작업
1. [구체적 작업 설명]
```
