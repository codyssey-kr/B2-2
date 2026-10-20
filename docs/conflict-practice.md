# 네 명의 충돌 해결 실습

1번은 `parkhojeong`의 해결·셀프리뷰 사례이며, 다른 세 명은 2·3·4번을 맡습니다.
각자 자기 폴더의 두 파일을 별도 PR로 진행합니다.
[1번의 실제 충돌 기록과 전후 검증](evidence/member-1-round-1/README.md)을 참고하되,
자신이 수행한 과정과 판단을 따로 기록합니다. 셀프리뷰는 타인의 승인 리뷰가 아닙니다.

## 파일과 브랜치

| 팀원 | 차수 | 파일 | 브랜치 |
|---|---|---|---|
| 1 | 1차 | `1/upper.py` | `feature/1-round-1` |
| 1 | 2차 | `1/lower.py` | `feature/1-round-2` |
| 2 | 1차 | `2/length.py` | `feature/2-round-1` |
| 2 | 2차 | `2/words.py` | `feature/2-round-2` |
| 3 | 1차 | `3/reverse.py` | `feature/3-round-1` |
| 3 | 2차 | `3/exclaim.py` | `feature/3-round-2` |
| 4 | 1차 | `4/first.py` | `feature/4-round-1` |
| 4 | 2차 | `4/last.py` | `feature/4-round-2` |

본인용 브랜치는 `feature/conflict-main`입니다.
공통 함수 `normalize_spaces()`는 `src/common.py`에 있습니다.
기존 `src/1_upper.py`부터 `src/4_words.py`까지는 새 폴더 구성으로 교체했습니다.

1·2·3번은 `feature/conflict-practice-setup`에서 갈라졌고,
4번은 두 파일을 추가한 후 공백 처리를 완성하기 전 커밋에서 갈라졌습니다.
main에 반영할 기준 구현은 각 파일의 공백 처리 줄을 `normalize_spaces(text)`로 바꿨고,
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
- 팀원은 병합 후 main에서 브랜치를 새로 만들지 않고 각자 준비된 작업 브랜치를 사용합니다.
  **2차 브랜치도 main 변경 전 기준으로 이미 준비되어 있어야 두 번째 충돌이 발생합니다.**

위 게시·병합 절차는 자동으로 수행되지 않습니다. 팀원이 아래 명령으로 받으려면
준비된 브랜치들이 원격에 게시되어 있어야 합니다.

## 2. 팀원별 1차 PR과 충돌 해결

아래는 이미 해결한 1번 사례의 절차입니다. 2·3·4번은 자신의 브랜치와 파일로 바꿔 진행합니다.
작업 Issue를 만들거나 기존 담당 Issue를 확인합니다.
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

팀원 2·3·4는 표의 1차 브랜치·파일로 같은 과정을 수행합니다.
기록 문서 충돌을 줄이려면 팀원 2 → 3 → 4 순서로 최신 main을 가져와 해결·기록·병합합니다.
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
팀원 2·3·4도 각각 `2/words.py`, `3/exclaim.py`, `4/last.py`로 진행합니다.
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
| `PYTHONPATH=. python3 4/first.py` | `Hello` |
| `PYTHONPATH=. python3 4/last.py` | `Team` |

빈 문자열과 공백뿐인 입력에서는 문자열 함수가 빈 문자열을, 개수 함수가 0을 반환해야 합니다.
단어 수·단어 뒤집기는 내부에서 split()을 사용하므로 출력이 같을 수도 있습니다.
출력만 보지 말고 공백 처리 코드의 차이와 팀의 일관된 처리 기준도 설명합니다.

## 평가 준비

- 각자 두 차례씩 수행하면 네 명의 충돌 기록은 총 8건입니다. 1번 1차는 사례로 기록했습니다.
- 준비 커밋만으로 팀원 기여가 완료되지는 않습니다. 실제 해결·기록·리뷰 반영 커밋을 남깁니다.
- 본인을 포함한 네 명 모두 PR 2개 이상 병합, 타인 PR 리뷰 2개 이상,
  본인 PR에서 리뷰 반영 최소 1회를 실제 링크로 확인합니다.
- 본인의 준비 PR·해결 PR과 각 팀원의 작성 PR은 실제 작성자와 병합 여부로 구분합니다.
- 충돌 실습이 amend/reset/revert/stash 실습을 대신하지는 않습니다.
  네 종류를 나누어 수행하고 전원이 최소 한 기록 작성에 참여합니다.
- `SUBMISSION.md`에 팀원별 Issue·PR·리뷰·반영·문서 링크와 Git 그래프 증빙을 모읍니다.

## 작업 참고 자료

각 팀원 브랜치의 `docs/tasks/팀원번호-round-차수.md`에서 담당 작업과 검증 기준을 확인합니다.
예를 들어 `feature/1-round-2`에는 `docs/tasks/1-round-2.md`가 있습니다.
이 문서는 이슈 본문 양식이 아닙니다. 각자 내용을 이해한 뒤 자신의 말로 목적·작업 범위·
완료 기준을 작성해 Issue를 만들고 PR에 연결합니다. 실제 수행 결과는 작업 후 기록합니다.

## 2차 Git 트러블슈팅

1번은 [2차 충돌 해결과 amend 사례](evidence/member-1-round-2/README.md)를 남겼습니다.
2번은 `reset --soft`, 3번은 `revert`, 4번은 `stash`와 `stash pop`을 직접 수행합니다.
각 작업 브랜치의 `docs/tasks/팀원번호-round-2.md`에 구체적인 순서를 적었습니다.
충돌 해결을 먼저 커밋해 깨끗한 상태를 만든 뒤 Git 실습을 진행합니다.
실제 상황·절차·결과·주의점은 `docs/troubleshooting-log.md`에 기록합니다.
팀원별 2차 Issue는 직접 작성하고 준비된 Draft PR에 연결합니다.
