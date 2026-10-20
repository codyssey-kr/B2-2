# 1번 · 1차 충돌 해결 사례

진행 계정은 `parkhojeong`입니다. 사용자 요청에 따라 Codex가 실제 Git 명령을
실행하고 결과를 수집했습니다. 자기 점검 사례이며, 타인의 승인 리뷰를 받은 기록은 아닙니다.

## 상황

- PR: https://github.com/codyssey-kr/B2-2/pull/12
- Issue: https://github.com/codyssey-kr/B2-2/issues/11
- 작업 브랜치: `feature/1-round-1`
- 병합 전 커밋: `83951874446bd155f2385c6236ffd825f0eafb6e`
- 병합 대상 main: `bb5ebb7184b774a032a000db70d851d538c7ba45`
- 충돌 파일: `1/upper.py`
- 해결 커밋: [a55e5a1](https://github.com/codyssey-kr/B2-2/commit/a55e5a160f6b0df628555401dd5f5dffc26cdf20)

작업 브랜치는 `text.strip()`으로 앞뒤 공백만 제거했고,
main은 `normalize_spaces(text)`로 연속 공백과 탭·줄바꿈까지 정리했습니다.
같은 줄을 서로 다르게 수정한 상태에서 `git merge --no-edit origin/main`을 실행했고
종료 코드 1과 실제 충돌 마커를 확인했습니다.

[conflict.json](conflict.json)에 병합 명령의 원문 출력, 충돌 마커가 포함된 전체 파일,
해결 전 입력별 결과를 저장했습니다.

## 해결 판단

이 함수의 요구사항은 앞뒤 공백을 없애고 내부 공백을 한 칸으로 통일한 뒤
대문자로 바꾸는 것입니다. `strip()`만 사용하면 `"  Hello   Team  "`의 내부 공백 세 칸이
그대로 남습니다. 따라서 `normalize_spaces(text)`를 선택하고 `text.upper()`는 유지했습니다.

main의 코드를 그대로 사용했지만, 선택 전에 두 구현의 의미와 입력별 결과를 비교했습니다.
충돌 마커를 제거한 것만으로 검증을 끝내지 않았습니다.

## 검증 결과

| 입력 | 해결 전 | 해결 후 |
|---|---|---|
| `"  Hello   Team  "` | `"HELLO   TEAM"` | `"HELLO TEAM"` |
| `" a\tB\nc "` | `"A\tB\nC"` | `"A B C"` |
| `""` | `""` | `""` |
| `" \t\n "` | `""` | `""` |
| `" 안녕  팀 "` | `"안녕  팀"` | `"안녕 팀"` |

`PYTHONPATH=. python3 1/upper.py`의 출력은 `HELLO TEAM`이었습니다.
[validation.json](validation.json)에 예상값과 실제값, 명령 출력과 종료 코드를 저장했습니다.

## 셀프리뷰

- 정상 입력뿐 아니라 빈 문자열, 공백뿐인 입력, 탭·줄바꿈, 한글 입력을 확인했습니다.
- 대문자 변환 동작과 공통 공백 정리 함수를 함께 유지했습니다.
- 실습 준비를 위한 충돌 해결과 타인이 남기는 리뷰·승인을 구분했습니다.
- 이후 팀원은 자신의 판단과 검증 결과를 별도로 남겨야 합니다.

## 재현 방법

아래는 현재 작업을 건드리지 않도록 별도 worktree에서 재현하는 명령입니다.
`../B2-2-conflict-replay`가 아직 존재하지 않을 때 사용합니다.

```sh
git worktree add --detach ../B2-2-conflict-replay 83951874446bd155f2385c6236ffd825f0eafb6e
cd ../B2-2-conflict-replay
git merge --no-commit bb5ebb7184b774a032a000db70d851d538c7ba45
git status
git diff -- 1/upper.py
```

충돌을 확인한 뒤에는 `git merge --abort`로 재현용 병합을 취소할 수 있습니다.
