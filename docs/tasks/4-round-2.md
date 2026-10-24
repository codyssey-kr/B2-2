# 팀원 4 · 2차 작업 참고

- 작업: 마지막 단어 찾기의 공백 처리 충돌 해결
- 브랜치: `feature/4-round-2`
- 대상 파일: `4/last.py`
- 함수: `last_word(text)`
- 기록 위치: `docs/conflict-resolution.md`의 `팀원 4 · 2차`

## 목표와 시작 조건

1번 해결 사례와 4번 기준 구현이 main에 병합된 뒤 시작합니다.
준비된 브랜치에서 최신 main을 병합하고, `text.strip()`과
`normalize_spaces(text)`가 같은 줄에서 충돌하는 것을 확인합니다.

[1번 사례](../evidence/member-1-round-1/README.md)를 참고해 직접 코드를 비교하고,
앞뒤 공백뿐 아니라 탭·줄바꿈과 연속 공백을 어떻게 처리할지 판단합니다.
새 main에서 브랜치를 다시 만들면 준비된 충돌이 사라질 수 있으므로 위 브랜치를 사용합니다.

## 검증

저장소 최상위에서 `PYTHONPATH=. python3 4/last.py`을 실행하면 `Team`가 나와야 합니다.

| 입력 | 예상 반환값 |
|---|---|
| `"  Hello   Team  "` | `Team` |
| `" a\tB\nc "` | `c` |
| `""` | `''` |
| `" \t\n "` | `''` |

## 기록

자신의 말로 Issue에 목적과 작업 범위를 정리하고 PR에 연결합니다.
충돌 코드, 해결 이유, 실행 명령·실제 결과, 참여자와 PR·커밋 링크를 남깁니다.
실질적인 리뷰에 답변·수정으로 응답합니다. 준비 커밋과 1번 사례는 본인의 수행 증빙이 아닙니다.

전체 명령과 순서는 [실습 안내](../conflict-practice.md)를 참고합니다.

## 2차 Git 실습: stash / stash pop

먼저 1차 PR을 마치고, 1번 2차 사례가 main에 들어온 뒤 이 브랜치의 코드 충돌을 해결합니다.
충돌 해결을 커밋하고 작업 트리가 깨끗한 것을 확인한 뒤 진행합니다.
아래에서는 이미 추적 중인 이 참고 문서에 미커밋 변경을 추가합니다.

```sh
printf '\n2차 stash 실습: 미커밋 변경 보관과 복원 확인\n' >> docs/tasks/4-round-2.md
git diff -- docs/tasks/4-round-2.md
git stash push -m "member 4 round 2 practice" -- docs/tasks/4-round-2.md
git stash list
git status --short
git switch --detach origin/main
git switch feature/4-round-2
git stash pop
git diff -- docs/tasks/4-round-2.md
```

중간에 다른 stash를 만들지 않고 방금 보관한 항목을 복원합니다.
보관 전·복원 후 diff가 같은지, 보관 중 작업 트리가 깨끗했는지 확인합니다.
`docs/troubleshooting-log.md`의 4번 항목에 stash 식별 정보, 실제 명령 출력,
브랜치 전환, 복원 결과와 주의점을 기록합니다. 복원된 문서와 기록을 커밋합니다.
이 안내 자체는 실습 완료 증빙이 아닙니다.
