# 네 명의 PR·충돌 해결 실습

A의 PR을 먼저 병합하고 B·C·D가 각자의 PR에서 충돌을 해결합니다.
네 브랜치는 모두 `feature/conflict-practice-setup`의 같은 커밋에서 시작하며,
`src/common.py`의 `normalize_spaces()` 설명 첫 줄을 서로 다르게 수정해 두었습니다.
함수 동작은 바꾸지 않았습니다.

이 브랜치와 설명 수정 커밋은 실습 준비물입니다. 팀원 본인의 구현, 리뷰,
리뷰 반영, 충돌 해결 기록을 대신하지 않습니다. 아직 충돌을 해결한 상태도 아닙니다.

## 시작 전

- 팀원 네 명의 역할 A·B·C·D를 정하고 저장소 작업 권한을 확인합니다.
- PR #8과 준비 브랜치의 문서 변경을 리뷰하고 `main`에 병합합니다.
- 이번 실습은 **Create a merge commit**으로 병합해 준비 브랜치의 이력을 유지합니다.
- `main`에 PR 필수와 작성자 외 승인 최소 1명을 설정합니다.
- 준비된 브랜치는 원격에 게시된 뒤 아래 명령으로 받을 수 있습니다.
  현재 원격 게시 여부는 저장소의 브랜치 목록에서 확인합니다.

## 역할과 작업

| 역할 | 브랜치 | 직접 구현할 작업 | 준비된 공통 함수 설명의 관점 | 리뷰 대상 |
|---|---|---|---|---|
| A | `feature/a-upper` | `src/1_upper.py`의 대문자 변환 수정 | 앞뒤 공백 제거 | B, C |
| B | `feature/b-lower` | `src/2_lower.py`의 소문자 변환 수정 | 탭·줄바꿈 처리 | C, D |
| C | `feature/c-length` | `src/3_length.py`의 글자 수 계산 수정 | 연속 공백 압축 | D, A |
| D | `feature/d-words` | `src/4_words.py`의 빈 입력 단어 수 수정 | 공백뿐인 입력 처리 | A, B |

설명의 관점은 모두 현재 공통 함수의 동작과 일치합니다.
충돌 해결 시 한쪽 내용을 무조건 버리지 말고 상대와 상의해 필요한 설명을 함께 담습니다.

## 1. 각자 구현하고 PR 열기

각자 자신의 작업 Issue를 만들고, 아래에서 역할에 맞는 브랜치만 선택합니다.
B를 기준으로 한 명령입니다. 이미 로컬 브랜치가 있다면 `git switch feature/b-lower`를 사용합니다.

```sh
git fetch origin
git switch --track origin/feature/b-lower
```

담당 함수의 오류를 수정하고 정상 입력과 경계 입력을 실행해 확인합니다.
예상 결과는 각 함수의 docstring에 있으며, D는 공백뿐인 입력이 `0`인지도 확인합니다.
수정한 파일만 커밋하고 자신의 브랜치에 push한 뒤 `main`을 대상으로 PR을 엽니다.

```sh
git add src/2_lower.py
git commit -m "fix: normalize text to lowercase"
git push -u origin feature/b-lower
```

PR에는 실제 Issue 번호를 사용한 `Closes #번호`, What, Why, 실행 명령과 결과를 적습니다.
리뷰어는 구체적인 코드에 근거한 의견을 남기고, 작성자는 답변과 필요한 수정으로 응답합니다.
각자 본인 PR에서 리뷰를 반영한 커밋과 답변 링크를 보관합니다.

**B·C·D는 A의 PR이 병합되기 전에 최신 main을 가져와 설명 차이를 없애지 않습니다.**
먼저 네 명의 PR을 준비하고 A를 리뷰·승인·병합합니다.

## 2. B → C → D 순서로 충돌 해결하기

A가 병합된 뒤 B가 먼저 아래 명령을 실행합니다.
커밋하지 않은 작업이 없는 상태에서 시작합니다.

```sh
git fetch origin
git switch feature/b-lower
git merge origin/main
git status
git diff -- src/common.py
```

`src/common.py`의 설명 줄에 충돌이 발생합니다.

1. A와 자신의 변경 의도를 공유합니다. C·D는 앞서 병합된 변경도 함께 확인합니다.
2. `<<<<<<<`, `=======`, `>>>>>>>` 사이의 양쪽 내용을 확인합니다.
3. 상대와 합의한 설명으로 직접 고치고 충돌 마커를 모두 제거합니다.
4. 아래 명령과 담당 함수의 사용 예시로 동작을 확인합니다.

```sh
python3 -m doctest src/common.py
python3 src/common.py "  Hello   Team  "
python3 src/2_lower.py
```

5. `docs/conflict-resolution.md`의 자기 기록에 실제 참여자, 충돌 내용,
   해결 이유, 명령, 검증 결과, PR 링크를 작성합니다.
6. 다음 명령으로 병합을 완료하고 기존 PR을 업데이트합니다.

```sh
git add src/common.py docs/conflict-resolution.md
git diff --cached --check
git diff --name-only --diff-filter=U
git commit -m "merge: resolve common utility description conflict"
git push
```

`git diff --name-only --diff-filter=U`에 출력이 있으면 아직 미해결 파일이 있는 것이므로
커밋 전에 해결합니다. 해결 커밋 링크는 이후 문서 수정이나 제출 인덱스에 보충합니다.

B의 PR을 다시 리뷰·승인·병합한 다음 C, 마지막으로 D가 같은 절차를 수행합니다.
C·D는 브랜치 이름과 담당 함수 실행 명령을 자신의 것으로 바꿉니다.
앞사람이 쓴 기록은 유지하고 자신의 기록만 채웁니다.
이 순서대로 진행하면 B·C·D가 각각 같은 파일의 같은 영역에서 충돌을 경험합니다.

## 3. 평가용 작업 마무리

- 이 흐름만으로는 팀원별 PR 2개 병합 기준이 끝나지 않습니다.
  첫 PR 병합 후 최신 `main`에서 두 번째 작업 브랜치를 만듭니다.
- 두 번째 PR은 실제 트러블슈팅 실습과 협업 문서 보완 등으로 나눌 수 있습니다.
  예: A는 amend, B는 reset, C는 revert, D는 stash를 수행하고
  `docs/troubleshooting-log.md`에 참여자·상황·절차·결과·주의점을 기록합니다.
- amend/reset은 아직 공개하지 않은 본인 커밋으로 실습합니다.
  revert는 공유된 커밋을 대상으로 수행하고, 보호된 main에 직접 push하지 않습니다.
- 팀원마다 PR 2개 이상 병합, 타인 PR 리뷰 2개 이상,
  본인 PR에서 리뷰 반영 최소 1회를 실제 링크로 확인합니다.
- `SUBMISSION.md`에 팀원별 Issue·PR·리뷰·리뷰 반영·문서 링크와
  `git log --oneline --graph --all` 증빙을 모읍니다.
- 준비 코드에는 의도적인 오류가 있으므로 정상 동작하는 최종 결과물과 구분합니다.
  준비본 병합만으로 main의 정상 동작 기준을 충족했다고 표시하지 않습니다.
