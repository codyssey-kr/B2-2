# 팀원 3 · 2차 작업 참고

- 작업: 느낌표 붙이기의 공백 처리 충돌 해결
- 브랜치: `feature/3-round-2`
- 대상 파일: `3/exclaim.py`
- 함수: `add_exclamation(text)`
- 기록 위치: `docs/conflict-resolution.md`의 `팀원 3 · 2차`

## 작업 목표

main의 `normalize_spaces(text)`와 작업 브랜치의 `text.strip()`이 같은 줄을
수정한 상태입니다. main을 병합하며 충돌을 확인하고, 두 코드의 동작을 비교한 뒤
팀에서 합의한 공백 처리 방식으로 해결합니다. 준비된 main의 요구사항은 앞뒤 공백을
제거하고 탭·줄바꿈을 포함한 연속 공백을 한 칸으로 정리하는 것입니다.

## 시작 조건

- main 작성자의 준비 PR이 먼저 main에 병합되어 있어야 합니다.
- 새 브랜치를 만들지 않고 위에 적힌 준비된 브랜치를 사용합니다.
- 2차 작업을 시작하기 전에 최신 원격 정보를 가져옵니다.
- 작업 트리가 깨끗한 상태에서 `git merge origin/main`을 수행합니다.
- 전체 순서와 명령은 [실습 안내](../conflict-practice.md)를 참고합니다.

## 검증 기준

저장소 최상위에서 실행합니다.

```sh
PYTHONPATH=. python3 3/exclaim.py
```

예상 출력은 `Hello Team!`입니다. 함수에 아래 입력도 직접 전달해 확인합니다.

| 입력 | 예상 반환값 |
|---|---|
| `"  Hello   Team  "` | `Hello Team!` |
| `" a\tB\nc "` | `a B c!` |
| `""` | `''` |
| `" \t\n "` | `''` |

## 작업을 마칠 때 확인할 내용

- 어떤 코드가 충돌했으며 왜 그 방식으로 해결했는지 설명할 수 있습니다.
- 정상 입력과 경계 입력의 실행 결과를 남깁니다.
- 실제 참여자, 충돌 내용, 해결 이유, 명령, PR·커밋 링크를 기록합니다.
- 앞서 병합된 다른 사람의 코드와 기록을 보존합니다.
- PR을 자신의 Issue와 연결하고 실질적인 리뷰에 답변·수정으로 응답합니다.

이 문서는 작업 참고용입니다. 그대로 등록하는 이슈 양식이나 완료 증빙이 아닙니다.
읽고 이해한 뒤 자신의 말로 목적·작업 범위·완료 기준을 정리해 Issue를 작성합니다.

## 2차 Git 실습: revert

먼저 1차 PR을 마치고, 1번 2차 사례가 main에 들어온 뒤 이 브랜치의 코드 충돌을 해결합니다.
충돌 해결을 커밋한 뒤 작업 트리가 깨끗한 상태에서 진행합니다.
다음 실습 파일이 아직 없을 때만 명령을 실행합니다.

```sh
mkdir -p docs/practice
printf '3번 revert 실습: 공개된 변경을 새 커밋으로 취소\n' > docs/practice/member-3-revert.md
git add docs/practice/member-3-revert.md
git commit -m "docs: add revert practice note"
git log -1 --oneline
git push -u origin feature/3-round-2
```

실습 커밋이 원격에 올라간 것을 확인하고 링크를 기록합니다.
이후 다른 커밋을 만들지 않은 상태에서 HEAD가 위 실습 커밋인지 확인한 뒤 되돌립니다.
충돌 해결 커밋이나 다른 사람의 변경을 되돌리지 않습니다.

```sh
git show --stat HEAD
git revert --no-edit HEAD
git log -2 --oneline
git status --short
git push
```

실습 파일이 삭제되고 원래 커밋과 revert 커밋이 모두 이력에 남는지 확인합니다.
`docs/troubleshooting-log.md`의 3번 항목에 전후 커밋과 원격 링크, 실제 명령,
결과, reset 대신 revert를 선택한 이유를 기록합니다.
main에 직접 push하거나 강제 push하지 않습니다. 이 안내는 수행 완료 증빙이 아닙니다.
