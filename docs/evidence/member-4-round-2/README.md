# 4번 · 2차 stash / stash pop 실습

진행 계정은 `sohye-pk`이며, Git 병합 충돌을 확인하고 미커밋 변경 사항을 stash와 stash pop으로 보관 및 복원하는 실습을 진행했습니다.

## 기준 이력

- Issue: https://github.com/codyssey-kr/B2-2/issues/29
- PR: https://github.com/codyssey-kr/B2-2/pull/34

- 브랜치: `feature/4-round-2-sohye`
- 병합 전 커밋: `02e0a70f7cabb418b67659c3a98511a672461539`
- 병합 후 커밋: `18bc3e28fd7554a5c8bcf67503057cd89beb39f5`
- 파일: `4/last.py`
- stash 대상 파일: `docs/tasks/4-round-2.md`
- stash 메시지: `member 4 round 2 practice`
- stash 식별 정보: `55b6ee1e43e4233710348280cb7d6839b14d572f`
- 
## 충돌 발생 및 해결 결과

`git merge --no-edit origin/main` 실행 중 `4/last.py`에서 공백 처리 방식이 달라 병합 충돌이 발생했습니다. 충돌 해결 후 `last_word` 함수의 일반 입력 및 경계 입력 4개를 검증했으며 모두 통과했습니다.

- 충돌 해결 전: 일반 문자열 입력 2개에서 기대한 마지막 단어가 반환되지 않았습니다.
- 충돌 해결 후: 4개 테스트 모두 기대 결과와 일치했습니다.
- 실행 명령: `PYTHONPATH=. python3 4/last.py`
- 실행 결과: 종료 코드 `0`, 출력 `Team`

자세한 충돌 내용과 테스트 결과는 `conflict.json`, `validation.json`에 기록했습니다.

## 변경 사항 보관

`docs/tasks/4-round-2.md` 파일 끝에 다음 문구를 추가했습니다.

```
2차 stash 실습: 미커밋 변경 보관과 복원 확인
```

`git diff -- docs/tasks/4-round-2.md`로 변경 사항을 확인한 뒤 다음 명령을 실행했습니다.

```sh
git stash push -m "member 4 round 2 practice" -- docs/tasks/4-round-2.md
git stash list
git status --short
```

실행 결과 `stash@{0}`에 보관 항목이 생성되었으며, `git status --short`의 출력이 비어 있어 작업 트리가 깨끗해진 것을 확인했습니다.

## 브랜치 전환과 변경 사항 복원

stash 보관 후 다음 순서로 브랜치를 전환했습니다.

```sh
git switch --detach origin/main
git switch feature/4-round-2-sohye
```

`origin/main`으로 detached HEAD 전환을 수행하고 원래 작업 브랜치로 돌아왔습니다.

이후 다음 명령으로 변경 사항을 복원했습니다.

```sh
git stash pop
git diff -- docs/tasks/4-round-2.md
```

복원 결과 `docs/tasks/4-round-2.md`가 미커밋 변경 상태로 표시되었으며, 추가했던 실습 문구가 diff에서 다시 확인되었습니다. 또한 `stash pop` 출력에서 해당 stash 항목이 제거된 것을 확인했습니다.

## 검증 결과

| 검증 항목 | 결과 |
| --- | --- |
| `origin/main` 병합 중 충돌 확인 | 확인 |
| 충돌 파일 및 충돌 마커 기록 | 확인 |
| 충돌 해결 후 테스트 | 확인 |
| 변경 사항 stash 보관 | 성공 |
| 보관 후 작업 트리 확인 | 변경 사항 없음 |
| 브랜치 전환 및 원래 브랜치 복귀 | 성공 |
| `stash pop`을 통한 변경 사항 복원 | 성공 |
| 복원 후 diff 확인 | 성공 |
| stash 항목 제거 | 성공 |

## 주의점과 선택 이유

- 병합 충돌은 두 브랜치에서 같은 코드 부분이 서로 다르게 수정되었을 때 발생할 수 있습니다.
- `strip()`과 `normalize_spaces()`의 공백 처리 범위는 다를 수 있으므로 공통 함수의 구현과 요구사항을 확인한 뒤 해결해야 합니다.
- `git stash`는 커밋하지 않은 변경 사항을 임시 보관해 작업 트리를 정리할 때 사용했습니다.
- 브랜치 전환 후 원래 브랜치로 돌아와 `git stash pop`으로 변경 사항을 복원했습니다.
- `stash pop`은 변경 사항을 적용하고 stash 항목을 제거하므로 복원 결과와 작업 트리 상태를 확인했습니다.

## 증빙

- [stash 실습 명령 및 전후 결과](stash.json)
