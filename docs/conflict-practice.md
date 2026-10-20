# 세 팀원이 두 번씩 충돌 해결하기

본인은 파일 여섯 개의 공백 처리를 완성해 먼저 main에 반영합니다.
세 팀원은 자기 폴더의 파일 두 개를 각각 별도 PR로 진행합니다.
한 사람당 PR 두 개에서 한 번씩, 총 두 번 충돌을 해결하는 구성입니다.

## 파일과 브랜치

| 팀원 | 차수 | 파일 | 브랜치 |
|---|---|---|---|
| 1 | 1차 | `1/upper.py` | `feature/1-round-1` |
| 1 | 2차 | `1/lower.py` | `feature/1-round-2` |
| 2 | 1차 | `2/length.py` | `feature/2-round-1` |
| 2 | 2차 | `2/words.py` | `feature/2-round-2` |
| 3 | 1차 | `3/reverse.py` | `feature/3-round-1` |
| 3 | 2차 | `3/exclaim.py` | `feature/3-round-2` |

본인용 브랜치는 `feature/conflict-main`입니다.
공통 함수 `normalize_spaces()`는 `src/common.py`에 있습니다.
기존 `src/1_upper.py`부터 `src/4_words.py`까지는 새 폴더 구성으로 교체했습니다.

일곱 작업 브랜치 모두 `feature/conflict-practice-setup`의 같은 커밋에서 시작합니다.
본인 브랜치는 여섯 파일의 공백 처리 줄을 `normalize_spaces(text)`로 바꿨고,
팀원 브랜치는 담당 파일 하나의 같은 줄을 `text.strip()`으로 바꿨습니다.
앞뒤 공백만 제거할지, 탭·줄바꿈·연속 공백도 정리할지 실제 동작을 비교하며 해결합니다.

준비된 커밋은 실습 재료입니다. 팀원 본인의 평가용 구현·리뷰·리뷰 반영·충돌 해결 기록을
대신하지 않으며, 충돌 해결과 문서 작성은 팀원이 직접 수행해야 합니다.

## 1. 본인 PR 먼저 병합

- 네 명의 저장소 작업 권한과 main의 PR 필수·작성자 외 승인 최소 1명을 확인합니다.
- `feature/conflict-main`을 main 대상으로 PR로 올리고 실제 작업 Issue를 연결합니다.
- 이 브랜치는 PR #8의 코드와 준비 문서까지 포함합니다. #8이 열려 있다면 대체 PR로
  정리하거나 #8 다음에 병합합니다. 준비 문서만 별도로 병합할 필요는 없습니다.
- 본인 PR을 리뷰·수정·승인한 뒤 **Create a merge commit**으로 병합합니다.
  이 실습의 후속 PR도 같은 방식으로 병합해 공통 이력을 유지합니다.
- 팀원은 병합 후 main에서 브랜치를 새로 만들지 않고 준비된 여섯 브랜치를 사용합니다.
  **2차 브랜치도 main 변경 전 기준으로 이미 준비되어 있어야 두 번째 충돌이 발생합니다.**

위 게시·병합 절차는 자동으로 수행되지 않습니다. 팀원이 아래 명령으로 받으려면
준비된 브랜치들이 원격에 게시되어 있어야 합니다.

## 2. 팀원별 1차 PR과 충돌 해결

팀원 1의 1차 작업 예시입니다. 먼저 자신의 작업 Issue를 만듭니다.
명령은 저장소 최상위 폴더에서 실행합니다.

```sh
git fetch origin
git switch --track origin/feature/1-round-1
```

이미 로컬 브랜치가 있다면 `git switch feature/1-round-1`을 사용합니다.
자기 브랜치로 main 대상 PR을 열고 실제 Issue 번호의 `Closes #번호`, What, Why,
검증 방법을 적습니다. 해결 전에는 Draft로 둘 수 있습니다.
커밋하지 않은 작업이 없는 상태에서 다음을 실행합니다.

```sh
git merge origin/main
git status
git diff -- 1/upper.py
```

`1/upper.py`의 공백 처리 줄에서 충돌이 발생합니다.

1. main 작성자와 `normalize_spaces(text)`와 `text.strip()`의 차이를 확인합니다.
2. `<<<<<<<`, `=======`, `>>>>>>>` 사이 양쪽 변경을 확인합니다.
3. 정상 입력, 빈 입력, 공백뿐인 입력, 탭·줄바꿈 입력을 비교합니다.
4. 앞뒤 공백 제거와 연속 공백 정리가 모두 필요한지 합의하고 코드를 수정합니다.
   준비된 main의 요구사항은 두 가지를 모두 수행하는 것입니다.
5. 충돌 마커를 제거하고 담당 파일을 실행합니다.

```sh
PYTHONPATH=. python3 1/upper.py
```

출력은 `HELLO TEAM`입니다. `PYTHONPATH=.`는 공통 함수를 가져올 수 있게
저장소 최상위를 모듈 검색 경로에 추가합니다.

6. `docs/conflict-resolution.md`의 본인·해당 차수에 실제 참여자, 충돌 내용,
   해결 이유, 명령, 검증 결과와 PR 링크를 적습니다.
7. 다음 명령으로 병합을 완료하고 자신의 PR을 업데이트합니다.

```sh
git add 1/upper.py docs/conflict-resolution.md
git diff --cached --check
git diff --name-only --diff-filter=U
git commit -m "merge: resolve uppercase whitespace conflict"
git push -u origin feature/1-round-1
```

미해결 파일 확인 명령에 출력이 있으면 커밋 전에 해결합니다.
해결 커밋 링크는 이후 문서 수정이나 제출 인덱스에 보충합니다.
타인의 실질적인 리뷰를 받고 의견에 답변·수정한 뒤 승인받아 병합합니다.

팀원 2와 3은 표의 1차 브랜치·파일로 같은 과정을 수행합니다.
기록 문서 충돌을 줄이려면 팀원 1 → 2 → 3 순서로 최신 main을 가져와 해결·기록·병합합니다.
다른 사람의 기능과 기록을 유지합니다.

## 3. 2차는 두 번째 파일과 준비된 두 번째 브랜치

1차가 끝난 뒤 각자 두 번째 작업 Issue와 PR을 만듭니다.
팀원 1의 예시입니다. **1차 브랜치나 최신 main에서 새 브랜치를 만들지 않습니다.**

```sh
git fetch origin
git switch --track origin/feature/1-round-2
git merge origin/main
git status
git diff -- 1/lower.py
```

이미 로컬 브랜치가 있다면 `git switch feature/1-round-2`를 사용합니다.
이번에는 `1/lower.py`의 공백 처리 줄에서 충돌을 해결합니다.
1차와 같은 절차로 검증하고, 기록 문서의 2차 항목을 채워 별도 PR을 리뷰·병합합니다.
팀원 2와 3도 각각 `2/words.py`, `3/exclaim.py`로 진행합니다.
이후 push할 때는 현재 차수의 브랜치 이름을 사용합니다.

## 실행 결과 확인

아래 명령은 저장소 최상위에서 실행하며, 공백 처리를 완료한 상태의 예상 결과입니다.

| 명령 | 예상 출력 |
|---|---|
| `PYTHONPATH=. python3 1/upper.py` | `HELLO TEAM` |
| `PYTHONPATH=. python3 1/lower.py` | `hello team` |
| `PYTHONPATH=. python3 2/length.py` | `10` |
| `PYTHONPATH=. python3 2/words.py` | `2` |
| `PYTHONPATH=. python3 3/reverse.py` | `Team Hello` |
| `PYTHONPATH=. python3 3/exclaim.py` | `Hello Team!` |

빈 문자열과 공백뿐인 입력에서는 문자열 함수가 빈 문자열을, 개수 함수가 0을 반환해야 합니다.
단어 수·단어 뒤집기는 내부에서 split()을 사용하므로 출력이 같을 수도 있습니다.
출력만 보지 말고 공백 처리 코드의 차이와 팀의 일관된 처리 기준도 설명합니다.

## 평가 준비

- 세 팀원은 각각 PR 두 개에서 충돌 두 번을 해결해 총 6건의 기록을 남깁니다.
- 준비 커밋만으로 팀원 기여가 완료되지는 않습니다. 실제 해결·기록·리뷰 반영 커밋을 남깁니다.
- 본인을 포함한 네 명 모두 PR 2개 이상 병합, 타인 PR 리뷰 2개 이상,
  본인 PR에서 리뷰 반영 최소 1회를 실제 링크로 확인합니다.
- 본인은 준비 PR 외에 트러블슈팅·협업 문서 등 추가 작업 PR이 필요합니다.
- 충돌 여섯 번이 amend/reset/revert/stash 실습을 대신하지는 않습니다.
  네 종류를 나누어 수행하고 전원이 최소 한 기록 작성에 참여합니다.
- `SUBMISSION.md`에 팀원별 Issue·PR·리뷰·반영·문서 링크와 Git 그래프 증빙을 모읍니다.
