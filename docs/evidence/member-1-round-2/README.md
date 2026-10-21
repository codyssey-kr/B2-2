# 1번 · 2차 충돌 해결 사례

진행 계정은 `parkhojeong`이며, 사용자 요청에 따라 Codex가 실제 명령과 검증을 실행했습니다.
1차와 다른 파일에서 발생한 두 번째 충돌입니다. 자기 점검과 타인의 승인 리뷰는 구분합니다.

## 기준 이력

- Issue: https://github.com/codyssey-kr/B2-2/issues/19
- PR: https://github.com/codyssey-kr/B2-2/pull/20
- 해결 커밋: https://github.com/codyssey-kr/B2-2/commit/03de96f29e20dcc30c3dbbbc8b739948e02ae6b1

- 브랜치: `feature/1-round-2`
- 병합 전 커밋: `d1e7c9cc7d579f68f5834cc570fbc7eb289139a1`
- 병합 대상 main: `aa2d9f612ea009550ae2bc9cec13c5b834a9b418`
- 파일: `1/lower.py`

## 충돌과 해결

`git merge --no-edit origin/main`을 실행해 종료 코드 1과 실제 충돌을 확인했습니다.
`text.strip()`과 `normalize_spaces(text)`가 같은 줄을 다르게 수정한 상태였습니다.
앞뒤 공백뿐 아니라 내부 연속 공백과 탭·줄바꿈도 정리해야 하므로 공통 함수를 선택했고,
소문자 변환 `text.lower()`는 유지했습니다.

[conflict.json](conflict.json)에 원문 명령 출력, 충돌 마커, 해결 전 결과를 보관했습니다.
[validation.json](validation.json)에 해결 후 예상값·실제값과 실행 출력을 보관했습니다.

| 입력 | 해결 전 | 해결 후 |
|---|---|---|
| `"  Hello   Team  "` | `"hello   team"` | `"hello team"` |
| `" A\tB\nC "` | `"a\tb\nc"` | `"a b c"` |
| `""` | `""` | `""` |
| `" \t\n "` | `""` | `""` |
| `" 안녕  팀 "` | `"안녕  팀"` | `"안녕 팀"` |

`PYTHONPATH=. python3 1/lower.py`의 실제 출력은 `hello team`이었습니다.

## 재현

아래 경로가 아직 존재하지 않을 때 별도 worktree에서 재현합니다.

```sh
git worktree add --detach ../B2-2-round-2-replay d1e7c9cc7d579f68f5834cc570fbc7eb289139a1
cd ../B2-2-round-2-replay
git merge --no-commit aa2d9f612ea009550ae2bc9cec13c5b834a9b418
git status
git diff -- 1/lower.py
```

확인 후 `git merge --abort`로 재현용 병합을 취소할 수 있습니다.

## amend 실습과 셀프리뷰

충돌 해결은 먼저 merge 커밋으로 마쳤습니다. 이후 별도의 미공개 문서 커밋을 만들고
`git commit --amend`로 메시지를 더 구체적으로 수정했습니다.
[amend.json](amend.json)에 실제 명령 출력과 전후 커밋·부모·파일 트리를 저장했습니다.
부모와 파일 트리는 같고 커밋 ID와 메시지는 달라진 것을 확인했습니다.

- 충돌 해결과 amend를 서로 다른 단계로 수행해 각 목적을 구분했습니다.
- 소문자 변환의 정상·경계 입력을 확인하고 원문 결과를 남겼습니다.
- 공개 전 커밋만 amend했으며 공유 이력은 다시 쓰지 않았습니다.
- 이 기록은 자기 점검이며 타인의 리뷰·승인 실적은 아닙니다.
