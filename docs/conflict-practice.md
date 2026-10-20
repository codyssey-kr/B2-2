# 본인 작업을 기준으로 세 팀원이 충돌 해결하기

본인의 기능 구현 PR을 먼저 main에 병합하고, 팀원 A·B·C는 각자 준비된
브랜치에서 최신 main을 병합하며 충돌을 해결합니다. D 역할은 없습니다.

## 브랜치 구성

| 담당 | 브랜치 | 준비된 변경 | 실제 수행할 작업 |
|---|---|---|---|
| 본인 | `feature/conflict-main` | 문자열 함수 4개의 오류 수정, 공통 함수 설명 변경 | 구현 검증, Issue 연결, PR 리뷰·반영 후 먼저 병합 |
| 팀원 A | `feature/a-upper` | 공통 함수 설명: 앞뒤 공백 제거 | 본인 PR 작성, main과 충돌 해결·기록 |
| 팀원 B | `feature/b-lower` | 공통 함수 설명: 탭·줄바꿈 처리 | 본인 PR 작성, main과 충돌 해결·기록 |
| 팀원 C | `feature/c-length` | 공통 함수 설명: 연속 공백 압축 | 본인 PR 작성, main과 충돌 해결·기록 |

네 브랜치는 `feature/conflict-practice-setup`의 같은 커밋에서 시작합니다.
`src/common.py`의 `normalize_spaces()` 설명 첫 줄을 서로 다르게 수정해 두었으므로,
본인 PR이 먼저 병합되면 A·B·C는 각자 같은 영역의 충돌을 경험합니다.
팀원은 함수 오류를 별도로 수정할 필요 없이 main의 완성된 구현을 가져옵니다.

준비된 커밋은 실습 재료이며 팀원 본인의 평가용 기여를 대신하지 않습니다.
각자 실제로 수행한 리뷰, 리뷰 반영, 충돌 해결과 기록을 남겨야 합니다.

## 1. 본인 작업을 먼저 main에 반영

- 네 명의 저장소 작업 권한과 main의 PR 필수·작성자 외 승인 최소 1명 설정을 확인합니다.
- `feature/conflict-main`을 main 대상으로 PR로 올리고, 실제 작업 Issue를 연결합니다.
- 이 브랜치는 PR #8의 코드와 준비 문서도 포함합니다. #8이 아직 열려 있다면
  대체 PR로 정리하거나, #8 이후 이 PR을 병합합니다. 준비 문서만 별도로 병합할 필요는 없습니다.
- 이번 실습의 PR은 **Create a merge commit**으로 병합해 공통 이력을 유지합니다.
- 본인 PR의 함수 동작과 설명을 팀원이 리뷰하고, 필요한 수정을 반영한 뒤 병합합니다.
- 이후 A·B·C는 새 main에서 브랜치를 다시 만들지 않고, 아래 준비된 브랜치를 사용합니다.

여기에 적힌 병합·게시 절차는 실제로 수행한 상태가 아닙니다.
브랜치가 원격에 게시되어 있어야 팀원이 아래 명령으로 받을 수 있습니다.

## 2. 팀원별 브랜치 받기

각자 작업 Issue를 만들고 아래 명령에서 자신의 브랜치를 선택합니다.
A를 기준으로 한 예시입니다. B·C는 표의 브랜치 이름으로 바꿉니다.
이미 로컬 브랜치가 있다면 `git switch feature/a-upper`만 실행합니다.

```sh
git fetch origin
git switch --track origin/feature/a-upper
```

자기 브랜치로 main 대상 PR을 열고, 실제 Issue 번호를 사용한 `Closes #번호`,
What, Why, 검증 방법을 적습니다. 충돌을 해결하는 동안은 Draft로 둘 수 있습니다.

## 3. A → B → C 순서로 충돌 해결

본인 PR이 main에 병합된 뒤 A가 먼저 진행합니다.
커밋하지 않은 작업이 없는 상태에서 실행합니다.

```sh
git fetch origin
git switch feature/a-upper
git merge origin/main
git status
git diff -- src/common.py
```

1. main 작성자와 자신의 설명 변경 의도를 공유합니다.
2. `<<<<<<<`, `=======`, `>>>>>>>` 사이의 양쪽 내용을 확인합니다.
3. 합의한 설명으로 직접 수정하고 충돌 마커를 모두 제거합니다.
   한쪽을 그대로 선택하기보다 각 변경의 의미를 확인해 필요한 설명을 함께 담습니다.
4. 아래 명령으로 가져온 함수 구현과 공통 함수의 동작을 확인합니다.

```sh
python3 -m doctest src/common.py
python3 src/common.py "  Hello   Team  "
python3 src/1_upper.py
python3 src/2_lower.py
python3 src/3_length.py
python3 src/4_words.py
```

출력은 차례대로 `Hello Team`, `HELLO TEAM`, `hello team`, `10`, `2`입니다.
빈 문자열과 공백뿐인 입력의 단어 수가 `0`인지도 별도로 확인합니다.

5. `docs/conflict-resolution.md`의 자기 기록에 실제 참여자, 충돌 내용,
   해결 이유, 명령, 검증 결과, PR 링크를 작성합니다.
6. 다음 명령으로 병합을 완료하고 자신의 PR을 업데이트합니다.

```sh
git add src/common.py docs/conflict-resolution.md
git diff --cached --check
git diff --name-only --diff-filter=U
git commit -m "merge: resolve common utility description conflict"
git push -u origin feature/a-upper
```

미해결 파일 확인 명령에 출력이 있으면 커밋 전에 해당 충돌을 해결합니다.
해결 커밋 링크는 이후 문서 수정이나 제출 인덱스에 보충합니다.

A의 PR을 리뷰·승인·병합한 다음 B, 마지막으로 C가 같은 절차를 수행합니다.
B·C는 main에 먼저 들어간 기능과 설명, 다른 사람의 기록을 함께 보존합니다.
각자 자기 기록만 채워 불필요한 문서 충돌을 줄입니다.

## 4. 평가용 기록 마무리

- 충돌 기록은 A·B·C 각 1회, 총 3회를 남길 수 있습니다.
  같은 파일의 같은 영역을 다르게 수정한 실제 충돌과 해결 증빙을 남깁니다.
- 본인을 포함한 네 명 모두 PR 2개 이상 병합, 타인 PR 리뷰 2개 이상,
  본인 PR에서 리뷰 반영 1회 이상을 별도로 충족해야 합니다.
- 리뷰는 본인 → A·B, A → B·C, B → C·본인, C → 본인·A처럼 나눌 수 있습니다.
  구체적인 코드 의견과 작성자의 답변·수정 링크를 남깁니다.
- 첫 PR 병합 후 최신 main에서 두 번째 작업 브랜치를 만듭니다.
  예를 들어 본인 amend, A reset, B revert, C stash를 실제 수행하고
  `docs/troubleshooting-log.md`에 상황·참여자·절차·결과·주의점을 기록합니다.
- amend/reset은 공개 전 본인 커밋으로 수행합니다. revert는 공유된 커밋을 대상으로
  수행하고, 보호된 main에 직접 push하지 않습니다.
- `SUBMISSION.md`에 팀원별 Issue·PR·리뷰·반영·문서 링크와 Git 그래프 증빙을 모읍니다.
