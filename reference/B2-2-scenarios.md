# B2-2 전체 실습 시나리오와 명령어

[프로젝트·실행 예시](../README.md) · [모범 답안](B2-2-checklist-answer.md) · [원문 체크리스트](B2-2-checklist.md)

**준비 → 첫 PR 4개 → A·B 실습 → C·D 실습 → 제출** 순서로 진행합니다.
이 문서는 앞으로 팀원이 실행할 절차이며 수행 완료 기록이 아닙니다.
보너스 과제인 rebase 히스토리 정리와 CODEOWNERS/리뷰어 자동화는 이번 실습에서 제외합니다.

- 명령은 macOS·Linux·WSL의 Bash 또는 zsh 기준이며, clone 이후에는 저장소 루트에서 실행합니다.
- A~D는 한 명씩 맡습니다. 자기 역할의 블록만 실행하고, 상대가 준비·병합할 때까지 기다리는 지점을 지킵니다.
- 코드는 편집기에서 직접 고칩니다. 예시의 `nano`는 평소 사용하는 편집기로 바꿔도 됩니다. nano는 Ctrl+O → Enter로 저장하고 Ctrl+X로 닫습니다.
- `task_*`, `pr_*`, `issue_body` 변수는 같은 터미널에서 이어집니다. 다시 열었다면 본인의 실제 Issue·PR URL과 역할 값을 다시 지정합니다.
- `git push`, `gh issue create`, `gh pr create/review/comment/merge/edit`는 실제 원격에 반영됩니다. 아래 문서를 읽는 것과 실제 실행을 구분합니다.
- 명령이 실패하거나 예상 결과가 다르면 다음 명령을 그대로 이어 실행하지 말고 현재 상태를 확인합니다.

| 단계 | 실행자 | 다음 단계로 넘어가는 조건 |
| --- | --- | --- |
| 0~1 | 전원·관리자 | 로그인·권한·main 보호·준비본 병합 확인 |
| 2~4 | 각 팀원과 리뷰어 | 네 사람의 함수 PR이 모두 Merged |
| 5의 A·B | A와 B, 리뷰어 D·A | A2 먼저 병합 → B가 충돌 해결 → B2 병합 |
| 5의 C·D | C와 D, 리뷰어 B·C | C2 먼저 병합 → D가 충돌 해결 → D2 병합 |
| 6 | 제출 정리 담당자·리뷰어 | 실제 증빙·링크를 모은 제출 PR 병합 |
| 7 | 필요할 때만 | 긴급 수정·실수 대응 |

[환경 준비](#setup) · [첫 작업](#first-task) · [PR·리뷰 공통 절차](#pr-cycle) · [A·B](#practice-ab) · [C·D](#practice-cd) · [제출](#submission) · [추가 상황](#extra)

<a id="setup"></a>

## 0. 전원: 도구와 로그인 확인

Git, Python 3.10 이상, GitHub CLI(`gh`)가 설치되어 있어야 합니다.
설치되지 않았다면 [GitHub CLI 설치 안내](https://cli.github.com/) 등을 통해 설치하고 돌아옵니다.

```sh
git --version
python3 --version
gh --version
gh auth status
```

로그인하지 않은 사람만 실행합니다. GitHub.com·HTTPS·브라우저 로그인을 선택합니다.

```sh
gh auth login
gh auth setup-git
```

### 저장소를 처음 받는 사람

```sh
git clone https://github.com/codyssey-kr/B2-2.git
cd B2-2
```

이미 받아 둔 사람은 해당 폴더로 이동합니다. 재clone하지 않습니다.

```sh
git remote -v
git status --short
git config user.name
git config user.email
```

origin이 팀 저장소인지 확인합니다. 이름·이메일이 없다면 아래 값을 **자기 정보로 바꿔** 설정합니다.

```sh
git config user.name "내 이름"
git config user.email "내 Git 커밋 이메일"
```

수정 파일이 있으면 본인 작업을 커밋하거나 보관한 뒤 브랜치를 바꿉니다.
아직 준비본이 main에 없다면 관리자의 1단계가 끝날 때까지 기다립니다.

## 1. 관리자: 권한·보호 규칙과 준비본 반영

```sh
gh repo view --web
```

브라우저에서 다음 설정을 실제로 확인합니다. 이 부분은 명령으로 임의 덮어쓰지 않고 GitHub 설정 화면에서 진행합니다.

1. 팀원 A~D의 쓰기·리뷰 권한과 기본 브랜치 main을 확인합니다.
2. main에 PR 필수·타인 승인 1명 이상·관리자 우회 제한을 설정하고 force push를 막습니다.
3. merge commit 방식의 PR 병합이 가능하도록 설정합니다.
4. 실제 설정 화면을 보관합니다. 제공되는 보호 기능은 저장소 공개 범위·요금제에 따라 확인합니다.

### 준비본이 아직 main에 없을 때만

현재 준비본 변경이 있는 로컬 저장소에서 시작합니다. 다른 작업이 섞이지 않았는지 확인하고, 팀원 실명·ID를 `SUBMISSION.md`에 적습니다.

```sh
git status --short
git switch -c feature/setup
nano SUBMISSION.md
```

```sh
task_title='docs: prepare team collaboration exercise'
issue_body=$(mktemp)
cat > "$issue_body" <<'ISSUE'
## 목적
공통 함수, 팀원 과제, 협업 문서와 실습 가이드를 팀 공통 기준으로 준비한다.

## 완료 기준
- 담당 파일을 변경하고 실행 결과 또는 실습 전후 상태를 기록한다.
- PR에서 이 이슈를 연결하고 타인 리뷰·응답·승인을 거쳐 병합한다.
ISSUE
task_issue_url=$(gh issue create --title "$task_title" --assignee @me --body-file "$issue_body")
task_issue_number=${task_issue_url##*/}
printf '%s\n' "$task_issue_url"
```

**확인:** 실제 Issue URL이 출력되어야 합니다. 실패하면 다음 단계로 넘어가지 말고 원인을 해결합니다. 같은 Issue를 이미 만들었다면 다시 만들지 말고 해당 URL·번호를 변수에 넣습니다.
```sh
python3 src/common.py "  Hello   team!  "
git add .gitignore .github README.md SUBMISSION.md src docs reference
git diff --cached --stat
git diff --cached --check
git commit -m "docs: prepare team collaboration exercise"
git push -u origin HEAD
```

공통 함수 출력 `Hello team!`와 staged 파일 범위를 확인한 뒤 커밋합니다. 준비본의 `src/`에는 정상 공통 함수와 의도적인 오류가 있는 팀원 함수 4개가 있습니다. 오류 수정 실습의 출발점이며, 아직 전체 기능이 정상인 상태는 아닙니다.
[3~4단계의 공통 PR·리뷰 절차](#pr-cycle)로 준비본 PR도 타인 리뷰 후 병합합니다. 이 PR은 팀원별 함수 구현 PR을 대신하지 않습니다.
준비본이 이미 main에 있다면 이 절차를 반복하지 않습니다.

<a id="first-task"></a>

## 2. 각 팀원: 함수 오류 수정과 첫 커밋

**전원:** 준비본 병합 후, 작업 트리가 깨끗한지 먼저 확인합니다.

```sh
git status --short
git switch main
git pull --ff-only origin main
python3 src/common.py "  Hello   team!  "
```

### 2-1. 내 역할 값 지정

아래 네 블록 중 **자기 것 하나만** 실행합니다.

**A**

```sh
task_branch='feature/a-upper'
task_file='src/1_upper.py'
task_title='feat: implement uppercase conversion'
```

**B**

```sh
task_branch='feature/b-lower'
task_file='src/2_lower.py'
task_title='feat: implement lowercase conversion'
```

**C**

```sh
task_branch='feature/c-length'
task_file='src/3_length.py'
task_title='feat: implement character count'
```

**D**

```sh
task_branch='feature/d-words'
task_file='src/4_words.py'
task_title='feat: implement word count'
```

### 2-2. Issue 생성 → 브랜치 → 구현

```sh
issue_body=$(mktemp)
cp .github/ISSUE_TEMPLATE/task.md "$issue_body"
nano "$issue_body"
```

파일 상단 `---` 사이의 템플릿 설정 부분은 지우고, 담당자·리뷰어·목적·작업 파일·완료 기준을 채웁니다.

```sh
task_issue_url=$(gh issue create --title "$task_title" --assignee @me --body-file "$issue_body")
task_issue_number=${task_issue_url##*/}
printf '%s\n' "$task_issue_url"
git fetch origin
git switch -c "$task_branch" origin/main
git branch --show-current
python3 "$task_file"
nano "$task_file"
```

Issue 생성 성공과 브랜치명을 확인합니다. 편집 전 첫 실행은 담당 파일의 오류를 재현하기 위한 것입니다.
초안은 실행되지만 A는 `Hello team`, B는 `HELLO TEAM`, C는 `9`가 나옵니다. D는 기본 입력에서는 `2`로 맞지만 빈 문자열 입력에서 `1`이 나옵니다.
각 초안의 의도적인 잘못된 반환식을 고치고, 파일 첫 docstring의 오류 초안 안내를 완성한 함수 설명으로 바꿉니다. 공통 함수 호출은 유지합니다.
수정 전후 결과를 PR의 How에 남기고 docstring에 빈 입력 등의 사용 예시도 적습니다. 정상 결과는 아래 표와 README를 기준으로 합니다.
**본인 담당 함수의 오류를 고치고 검증한 뒤 병합합니다. 네 사람의 첫 PR이 모두 병합되면 전체 함수가 정상 결과를 내야 합니다.**

```sh
python3 "$task_file"
```

기본 예상 출력은 A `HELLO TEAM`, B `hello team`, C `10`, D `2`입니다.
파일 하단 입력을 `""`, `"   "`, `"안녕 팀원들"`로 바꿔 실행하고 [예상 결과](../README.md#examples)와 비교합니다.
각 결과를 메모한 다음 하단 입력은 원래 `"  Hello   Team  "`으로 복원합니다.

### 2-3. 커밋과 push

```sh
git diff -- "$task_file"
git add "$task_file"
git diff --cached --check
git diff --cached
git commit -m "$task_title"
git push -u origin HEAD
```

**완료 조건:** 내 함수와 docstring 변경만 커밋되고, 본인 feature 브랜치가 원격에 있습니다. 다음은 PR 생성입니다.

<a id="pr-cycle"></a>

## 3. 작성자: PR 생성 — 모든 작업에 공통

첫 PR, 준비본 PR, 두 번째 PR, 제출 PR에서 같은 절차를 사용합니다.
각 작업의 `task_title`, `task_issue_url`, `task_issue_number`가 올바른지 확인합니다.
터미널을 다시 열었다면 실제 값으로 복구합니다. 예시 문구를 그대로 게시하지 않습니다.

```sh
git branch --show-current
printf '%s\n' "$task_title" "$task_issue_url" "$task_issue_number"
pr_body=$(mktemp)
cp .github/pull_request_template.md "$pr_body"
nano "$pr_body"
```

본문의 `Closes #...`를 실제 Issue 번호로 바꾸고 What·Why·How를 채웁니다.
How에는 실행한 명령·입력·예상 결과·실제 출력을, 실습 PR에는 기록 문서 경로·전후 커밋을 넣습니다.
체크박스는 이미 확인한 것만 표시합니다.

```sh
git push -u origin HEAD
task_branch=$(git branch --show-current)
task_pr_url=$(gh pr create --base main --head "$task_branch" --title "$task_title" --body-file "$pr_body")
printf '%s\n' "$task_pr_url"
gh pr view "$task_pr_url" --web
```

실제 PR URL을 리뷰어에게 전달하고 본인이 보관합니다. 이미 PR을 만들었다면 `gh pr view --json url --jq .url`로 URL을 확인해 변수에 넣으며 중복 생성하지 않습니다.
[PR 생성 명령 참고](https://cli.github.com/manual/gh_pr_create)

| 작성자 | 첫 PR 리뷰어 | 두 번째 PR 리뷰어 |
| --- | --- | --- |
| A | B | D |
| B | C | A |
| C | D | B |
| D | A | C |

## 4. 리뷰어·작성자: 코멘트 → 수정 → 승인 → 병합

### 4-1. 리뷰어 계정으로 검토

아래 URL은 전달받은 실제 값으로 바꿉니다. 자기 PR에는 리뷰하지 않습니다.

```sh
review_pr_url='실제 리뷰할 PR URL'
gh pr view "$review_pr_url"
gh pr diff "$review_pr_url"
gh pr view "$review_pr_url" --web
review_body=$(mktemp)
nano "$review_body"
```

파일·함수·라인에 근거한 구체적인 의견을 작성합니다. 예: “`count_characters`가 중간 공백도 세는지 사용 예시를 보완해 주세요.” 실제 변경에서 필요한 내용을 씁니다.

```sh
gh pr review "$review_pr_url" --comment --body-file "$review_body"
```

코드 라인에 붙이는 리뷰와 해당 스레드의 답글은 열린 브라우저에서 작성할 수 있습니다.
CLI의 `--comment`는 PR 전체에 대한 리뷰입니다. 수정이 필수라면 `--request-changes`를 대신 사용할 수 있습니다.
[리뷰 명령 참고](https://cli.github.com/manual/gh_pr_review)

### 4-2. 작성자가 의견 반영

본인 작업 브랜치에서 의견을 읽고 해당 파일을 편집합니다. 첫 PR의 경우:

```sh
gh pr view "$task_pr_url" --comments
nano "$task_file"
python3 "$task_file"
git add "$task_file"
git diff --cached --check
git commit -m "docs: clarify utility behavior after review"
git push origin HEAD
git rev-parse HEAD
```

커밋 메시지는 실제 변경이 코드 수정이면 `fix: ...` 등으로 바꿉니다. 변경이 없다면 빈 커밋을 만들지 않습니다.
실습·제출 PR에서는 해당 문서를 편집하고 그 파일을 `git add`합니다. 코드 수정 시에는 실행 결과도 다시 확인합니다.

```sh
reply_body=$(mktemp)
nano "$reply_body"
gh pr comment "$task_pr_url" --body-file "$reply_body"
```

답글에 무엇을 어떻게 반영했는지와 수정 커밋 SHA를 적습니다. 이 명령은 PR 전체 댓글이므로 특정 리뷰 스레드의 답글은 브라우저에서 남깁니다.
**각자 최소 한 번은 실제 수정 반영**을 해야 합니다. 실행 결과가 달라졌다면 PR의 How도 갱신합니다.

### 4-3. 리뷰어의 최종 승인

```sh
gh pr diff "$review_pr_url"
gh pr view "$review_pr_url" --comments
approval_body=$(mktemp)
nano "$approval_body"
gh pr review "$review_pr_url" --approve --body-file "$approval_body"
```

반영된 내용과 확인한 결과를 승인 설명에 적습니다. 수정 요청을 했던 리뷰어도 최종 변경을 확인합니다.

### 4-4. 작성자가 병합하고 결과 확인

```sh
gh pr view "$task_pr_url" --json state,reviewDecision,mergeable,url
gh pr merge "$task_pr_url" --merge
gh pr view "$task_pr_url" --json state,mergedAt,mergeCommit,url
```

승인·실행 확인·충돌 해결이 끝난 경우에만 병합합니다. 보호 규칙 때문에 막히면 원인을 해결하며 `--admin`으로 우회하지 않습니다.
**최종 state가 `MERGED`여야 완료**입니다. 대기 상태는 병합 완료로 세지 않습니다. [병합 명령 참고](https://cli.github.com/manual/gh_pr_merge)

PR·리뷰 스레드·반영 커밋 URL을 제출용으로 보관합니다. 첫 PR 네 개가 모두 병합되면 5단계로 진행합니다.

<a id="practice"></a>

## 5. 두 번째 PR: Git 실습

**시작 조건:** A1~D1이 모두 main에 병합되어 있어야 합니다.
실행 순서는 **A·B 준비 → A2 병합 → B가 충돌 해결·B2 병합 → C·D 준비 → C2 병합 → D가 충돌 해결·D2 병합**입니다.
아래 예상 결과는 안내입니다. 실제 명령·출력은 수행 후 기록합니다.
충돌 출력은 위아래 코드 울타리를 포함해 각 줄 앞에 `> `를 붙인 인용 블록으로 기록하고, 줄 끝 공백은 제거합니다.
일반 코드 블록 안에 마커를 그대로 붙이면 `git diff --cached --check`가 기록용 마커도 미해결 충돌로 판단합니다. 아래 마커 예시와 같은 형식을 사용합니다.
모든 명령은 저장소 루트의 본인 feature 브랜치에서 실행합니다. 각 Issue 생성 결과는 본인 터미널의 `task_issue_url`, `task_issue_number`에 보관합니다.
충돌 2회 모두 README의 같은 줄을 서로 수정하는 방식입니다. 같은 hunk 충돌이므로 미션의 비자명 충돌 기준에도 해당합니다.

[A·B 준비](#practice-ab) → [A 실습](#practice-a) → [B 실습](#practice-b) → [C·D 준비](#practice-cd) → [C 실습](#practice-c) → [D 실습](#practice-d)

### 담당 작업

| 역할 | Issue 제목 | 담당 실습 | 작성할 기록 / 보완할 협업 규칙 |
| --- | --- | --- | --- |
| A | `docs: 프로젝트 소개와 amend 실습 기록` | README 소개 수정, 최근 커밋 메시지 수정 | 트러블슈팅 T1 / 브랜치 규칙 |
| B | `docs: 소개 문구 충돌과 reset 실습 기록` | 같은 소개 줄 수정, 로컬 커밋 취소·재커밋, 충돌 #1 해결 | 트러블슈팅 T2·충돌 #1 / 커밋 규칙 |
| C | `docs: 실행 예시와 revert 실습 기록` | README 실행 예시 수정, 원격 feature 커밋 취소 | 트러블슈팅 T3 / PR 규칙 |
| D | `docs: 예시 충돌과 stash 실습 기록` | 같은 실행 예시 수정, 작업 보관·복구, 충돌 #2 해결 | 트러블슈팅 T4·충돌 #2 / 리뷰·충돌 규칙 |

각자 `docs/CONTRIBUTING.md`의 담당 규칙을 읽고 팀이 합의한 내용으로 보완합니다.
기록에는 실제 이름·역할·명령·출력·전후 커밋·관련 URL을 넣습니다.

<a id="practice-ab"></a>

### 1. A와 B가 함께 준비

A와 B는 작업 트리가 깨끗한지 확인하고 실행합니다. 2차 Issue는 각자의 아래 단계에서 만듭니다.

```sh
git status --short
git fetch origin
git rev-parse origin/main
```

두 사람의 SHA가 같은지 확인하고 **A2가 병합되기 전에 둘 다 브랜치를 만듭니다.**

| 담당 | 본인만 실행할 명령 |
| --- | --- |
| A | `git switch -c feature/a-intro origin/main` |
| B | `git switch -c feature/b-intro origin/main` |

A와 B가 각각 브랜치를 만들었다고 확인한 뒤 2~3단계를 진행합니다.
예정된 충돌 단계 전에는 브랜치를 자동 갱신하거나 main을 먼저 합치지 않습니다.

<a id="practice-a"></a>

### 2. A: 소개 수정 → amend → A2 병합

```sh
task_title='docs: revise introduction and record amend'
issue_body=$(mktemp)
cat > "$issue_body" <<'ISSUE'
## 목적
README 소개 수정과 미공개 커밋 메시지 수정을 수행하고 T1 및 브랜치 규칙을 기록한다.

## 완료 기준
- 담당 파일을 변경하고 실행 결과 또는 실습 전후 상태를 기록한다.
- PR에서 이 이슈를 연결하고 타인 리뷰·응답·승인을 거쳐 병합한다.
ISSUE
task_issue_url=$(gh issue create --title "$task_title" --assignee @me --body-file "$issue_body")
task_issue_number=${task_issue_url##*/}
printf '%s\n' "$task_issue_url"
```

**확인:** 실제 Issue URL이 출력되어야 합니다. 실패하면 다음 단계로 넘어가지 말고 원인을 해결합니다. 같은 Issue를 이미 만들었다면 다시 만들지 말고 해당 URL·번호를 변수에 넣습니다.

1. 루트 `README.md` 제목 바로 아래의 소개 문장 한 줄을 다음 문장으로 바꿉니다.

   `4명이 간단한 Python 함수를 구현하며 Git 협업을 연습합니다.`

2. `nano README.md`로 편집한 뒤 아래 명령으로 소개 변경만 커밋합니다. 아직 push하지 않습니다.

```sh
git add README.md
git commit -m "docs: describe Python function practice"
git status --short
git log -1 --format='%h %s'
git rev-parse 'HEAD^{tree}'
git commit --amend -m "docs: clarify the project introduction"
git log -1 --format='%h %s'
git rev-parse 'HEAD^{tree}'
```

**확인:** 커밋 SHA·메시지는 바뀌고 tree SHA(파일 내용)는 같습니다.
전후 출력을 복사해 [트러블슈팅 기록](../docs/troubleshooting-log.md)의 T1을 채웁니다.
CONTRIBUTING.md의 브랜치 규칙도 팀 합의에 맞게 보완합니다.

```sh
nano docs/troubleshooting-log.md docs/CONTRIBUTING.md
git add docs/troubleshooting-log.md docs/CONTRIBUTING.md
git commit -m "docs: record amend exercise and branch agreement"
git push -u origin HEAD
```

**A는 [3~4단계 명령](#pr-cycle)으로 PR 생성 → D 리뷰 → A 응답·수정 → D 승인 → 병합을 진행합니다.** 본인 2차 Issue 번호를 연결하고 최종 `MERGED` 상태를 확인합니다.
**병합되었다고 B에게 알려 줍니다.**

<a id="practice-b"></a>

### 3. B: 소개 수정 → reset → A 변경과 충돌 해결

```sh
task_title='docs: resolve introduction conflict and record reset'
issue_body=$(mktemp)
cat > "$issue_body" <<'ISSUE'
## 목적
README 소개 충돌을 해결하고 T2·충돌 기록 #1·커밋 규칙을 기록한다.

## 완료 기준
- 담당 파일을 변경하고 실행 결과 또는 실습 전후 상태를 기록한다.
- PR에서 이 이슈를 연결하고 타인 리뷰·응답·승인을 거쳐 병합한다.
ISSUE
task_issue_url=$(gh issue create --title "$task_title" --assignee @me --body-file "$issue_body")
task_issue_number=${task_issue_url##*/}
printf '%s\n' "$task_issue_url"
```

**확인:** 실제 Issue URL이 출력되어야 합니다. 실패하면 다음 단계로 넘어가지 말고 원인을 해결합니다. 같은 Issue를 이미 만들었다면 다시 만들지 말고 해당 URL·번호를 변수에 넣습니다.

A2 병합 전 만들어 둔 `feature/b-intro`에서 시작합니다.
A와 같은 소개 줄을 다음 문장으로 바꿉니다.

`4명이 PR과 코드 리뷰를 통해 Git 협업을 연습합니다.`

`nano README.md`로 편집합니다. 아래 reset은 방금 만든 **미공개 소개 커밋 하나**만 취소하는 실습입니다.

```sh
git add README.md
git commit -m "docs: describe PR and review practice"
git show --stat HEAD
git rev-parse HEAD
git rev-parse HEAD~1
git rev-parse 'HEAD^{tree}'
git reset --soft HEAD~1
git rev-parse HEAD
git status --short
git diff --cached
git write-tree
git commit -m "docs: emphasize PR and review collaboration"
```

**확인:** HEAD가 이전 부모 커밋으로 돌아가고 변경은 staged 상태에 남습니다.
reset 전 tree SHA와 `git write-tree` 결과가 같아야 합니다. 그 변경을 다시 커밋한 상태입니다.
`--hard`로 바꾸지 않습니다.
T2에 실제 출력을 적고 CONTRIBUTING.md의 커밋 규칙을 보완한 뒤 저장합니다.

```sh
nano docs/troubleshooting-log.md docs/CONTRIBUTING.md
git add docs/troubleshooting-log.md docs/CONTRIBUTING.md
git commit -m "docs: record soft reset exercise and commit agreement"
```

#### A2가 병합된 다음 실행

```sh
git status --short
# 비어 있어야 함
git fetch origin
git merge origin/main
git status
git diff -- README.md
```

**예상:** 같은 소개 줄을 서로 다른 문장으로 바꿔 충돌합니다. 마커의 핵심은 다음과 같습니다.

> ```text
> <<<<<<< HEAD
> 4명이 PR과 코드 리뷰를 통해 Git 협업을 연습합니다.
> =======
> 4명이 간단한 Python 함수를 구현하며 Git 협업을 연습합니다.
> >>>>>>> origin/main
> ```

위쪽은 B의 현재 브랜치, 아래쪽은 main에 병합된 A의 변경입니다.
A와 B가 함께 두 의도를 담은 최종 문장을 정합니다. 예를 들어
`4명이 간단한 Python 함수를 구현하고 PR과 코드 리뷰로 Git 협업을 연습합니다.`로 합칠 수 있습니다.
마커를 제거하고 [충돌 기록](../docs/conflict-resolution.md)의 #1에 원인·명령·마커·합의 이유·최종 내용을 적습니다.
다른 문서에도 충돌이 있으면 A와 B의 기록을 모두 보존합니다.

```sh
nano README.md docs/conflict-resolution.md
git add README.md docs/conflict-resolution.md
# 다른 충돌 파일을 해결했다면 그 파일도 git add
git diff --name-only --diff-filter=U
# 출력이 없어야 다음으로 진행
git diff --cached --check
```

다음 명령의 예상 결과가 A `HELLO TEAM`, B `hello team`, C `10`, D `2`인지 확인합니다.

```sh
python3 src/1_upper.py
python3 src/2_lower.py
python3 src/3_length.py
python3 src/4_words.py
```

확인 후 마칩니다.

```sh
git commit -m "docs: combine implementation and review goals"
git push -u origin HEAD
```

**B는 [3~4단계 명령](#pr-cycle)으로 PR 생성 → A 리뷰 → B 응답·수정 → A 승인 → 병합을 진행합니다.** 본인 2차 Issue 번호를 연결하고 최종 `MERGED` 상태를 확인합니다.
**A2·B2가 모두 병합된 다음 C와 D가 시작합니다.**

<a id="practice-cd"></a>

### 4. C와 D가 함께 준비

C와 D는 깨끗한 작업 트리에서 실행합니다. 2차 Issue는 각자의 아래 단계에서 만듭니다.

```sh
git fetch origin
git rev-parse origin/main
```

두 사람의 SHA가 같은지 확인하고 **C2가 병합되기 전에 둘 다 브랜치를 만듭니다.**

| 담당 | 본인만 실행할 명령 |
| --- | --- |
| C | `git switch -c feature/c-examples origin/main` |
| D | `git switch -c feature/d-examples origin/main` |

두 브랜치의 README의 “공통 함수 실행” 섹션에 `python3 src/common.py "  Hello   team!  "` 예시가 그대로 있는지 확인합니다.
C와 D는 같은 명령 줄을 다르게 수정합니다. 브랜치를 만든 뒤 5~6단계를 진행합니다.

<a id="practice-c"></a>

### 5. C: 예시 수정 → 원격 커밋 revert → C2 병합

```sh
task_title='docs: revise example and record revert'
issue_body=$(mktemp)
cat > "$issue_body" <<'ISSUE'
## 목적
공통 함수 실행 예시를 수정하고 원격 임시 안내 커밋을 취소해 T3·PR 규칙을 기록한다.

## 완료 기준
- 담당 파일을 변경하고 실행 결과 또는 실습 전후 상태를 기록한다.
- PR에서 이 이슈를 연결하고 타인 리뷰·응답·승인을 거쳐 병합한다.
ISSUE
task_issue_url=$(gh issue create --title "$task_title" --assignee @me --body-file "$issue_body")
task_issue_number=${task_issue_url##*/}
printf '%s\n' "$task_issue_url"
```

**확인:** 실제 Issue URL이 출력되어야 합니다. 실패하면 다음 단계로 넘어가지 말고 원인을 해결합니다. 같은 Issue를 이미 만들었다면 다시 만들지 말고 해당 URL·번호를 변수에 넣습니다.

1. README의 “공통 함수 실행” 섹션의 공통 함수 실행 명령 입력을 `"  Python   team!  "`으로 바꿉니다.
2. 바로 아래 설명의 예상 출력도 `Python team!`로 바꿉니다.
3. `nano README.md`로 편집하고 변경을 커밋합니다.

```sh
git add README.md
git commit -m "docs: use Python in the common utility example"
```

작업 트리가 깨끗한 상태에서 README 끝에 임시 안내 한 줄을 추가하고 **원격에 공개한 뒤** 취소합니다.

```sh
printf '\n%s\n' 'revert 실습용 임시 안내' >> README.md
git add README.md
git commit -m "docs: add temporary notice for revert exercise"
revert_target=$(git rev-parse HEAD)
git push -u origin HEAD
git fetch origin
git branch -r --contains "$revert_target"
```

**확인:** 출력에 `origin/feature/c-examples`가 있어야 합니다. 없으면 다음 단계로 넘어가지 않습니다.
같은 터미널에서 계속 실행합니다. 다시 열었다면 방금 push한 임시 안내 커밋 SHA를 `revert_target`에 넣습니다.

```sh
git revert --no-edit "$revert_target"
git log -2 --oneline
git status --short
git push origin HEAD
```

**확인:** README의 임시 안내 줄은 없어지고, 앞에서 바꾼 Python 예시는 남습니다.
원본 커밋과 취소 커밋도 모두 히스토리에 남습니다.
원격에 공개한 커밋을 새 커밋으로 취소하므로 force push가 필요하지 않습니다.
이번 대상은 임시 안내를 추가한 일반 커밋이며 PR의 merge 커밋이 아닙니다.
T3에 전후 출력·원본 커밋 URL·취소 커밋 URL을 적고 CONTRIBUTING.md의 PR 규칙을 보완합니다.

```sh
nano docs/troubleshooting-log.md docs/CONTRIBUTING.md
git add docs/troubleshooting-log.md docs/CONTRIBUTING.md
git commit -m "docs: record revert exercise and PR agreement"
git push origin HEAD
```

**C는 [3~4단계 명령](#pr-cycle)으로 PR 생성 → B 리뷰 → C 응답·수정 → B 승인 → 병합을 진행합니다.** 본인 2차 Issue 번호를 연결하고 최종 `MERGED` 상태를 확인합니다.
**병합되었다고 D에게 알려 줍니다.** 로컬 revert만 수행하면 원격 커밋 취소 실습을 완료한 것이 아닙니다.

<a id="practice-d"></a>

### 6. D: 예시 수정 → stash → 같은 명령 줄의 충돌 해결

```sh
task_title='docs: resolve example conflict and record stash'
issue_body=$(mktemp)
cat > "$issue_body" <<'ISSUE'
## 목적
작업 보관·복구와 README 실행 예시 충돌을 해결하고 T4·충돌 기록 #2·리뷰 규칙을 기록한다.

## 완료 기준
- 담당 파일을 변경하고 실행 결과 또는 실습 전후 상태를 기록한다.
- PR에서 이 이슈를 연결하고 타인 리뷰·응답·승인을 거쳐 병합한다.
ISSUE
task_issue_url=$(gh issue create --title "$task_title" --assignee @me --body-file "$issue_body")
task_issue_number=${task_issue_url##*/}
printf '%s\n' "$task_issue_url"
```

**확인:** 실제 Issue URL이 출력되어야 합니다. 실패하면 다음 단계로 넘어가지 말고 원인을 해결합니다. 같은 Issue를 이미 만들었다면 다시 만들지 말고 해당 URL·번호를 변수에 넣습니다.

C2 병합 전 만들어 둔 `feature/d-examples`에서 시작합니다.
README의 “공통 함수 실행” 섹션의 같은 명령 입력을 `"  Git   team!  "`으로 바꾸고, 바로 아래 예상 출력도 `Git team!`로 바꿉니다.
`nano README.md`로 편집하고, 아직 커밋하지 않은 상태로 작업을 잠시 보관합니다.

```sh
git diff -- README.md
git stash push -u -m "D2 Git example before branch switch"
git stash list
git status --short
# 비어 있어야 브랜치 전환
git switch main
python3 src/common.py "  team   work  "
git switch feature/d-examples
git stash pop
git diff -- README.md
git stash list
```

**확인:** stash 전후 변경이 같고, 성공한 pop 이후 해당 stash가 목록에서 사라집니다.
실습 중 다른 stash를 새로 만들지 않습니다. pop 충돌이 나면 stash가 남을 수 있으므로 복구 확인 전 drop하지 않습니다.
T4를 기록하고 CONTRIBUTING.md의 리뷰·충돌 규칙을 보완합니다.

```sh
nano docs/troubleshooting-log.md docs/CONTRIBUTING.md
git add README.md docs/troubleshooting-log.md docs/CONTRIBUTING.md
git commit -m "docs: update the example and record stash exercise"
```

#### C2가 병합된 다음 실행

```sh
git status --short
# 비어 있어야 함
git fetch origin
git merge origin/main
git status
git diff -- README.md
```

**예상:** 같은 명령 줄을 C는 Python, D는 Git으로 바꿔 내용 충돌이 발생합니다.
실제 `git status`와 `git diff`의 마커를 기록합니다. 핵심은 다음과 같습니다.

> ```text
> <<<<<<< HEAD
> python3 src/common.py "  Git   team!  "
> =======
> python3 src/common.py "  Python   team!  "
> >>>>>>> origin/main
> ```

C와 D가 합의해 두 실행 명령을 모두 남기고 각각의 예상 출력도 함께 적습니다.
충돌 마커는 제거합니다. 같은 파일 안의 예상 출력 설명에도 마커가 있으면 모두 해결합니다.
충돌 기록 #2에 원인·명령·합의·최종 내용을 적습니다. 다른 충돌 문서도 양쪽 기록을 보존합니다.

```sh
nano README.md docs/conflict-resolution.md
git add README.md docs/conflict-resolution.md
# 다른 충돌 파일을 해결했다면 그 파일도 git add
git diff --name-only --diff-filter=U
# 출력이 없어야 다음으로 진행
git diff --cached --check
```

README에 남긴 두 예시와 팀원 함수를 실행합니다.

```sh
python3 src/common.py "  Python   team!  "
python3 src/common.py "  Git   team!  "
python3 src/1_upper.py
python3 src/2_lower.py
python3 src/3_length.py
python3 src/4_words.py
```

예상 출력은 `Python team!`, `Git team!`, `HELLO TEAM`, `hello team`, `10`, `2`입니다. 확인 후 마칩니다.

```sh
git commit -m "docs: preserve both common utility examples"
git push -u origin HEAD
```

**D는 [3~4단계 명령](#pr-cycle)으로 PR 생성 → C 리뷰 → D 응답·수정 → C 승인 → 병합을 진행합니다.** 본인 2차 Issue 번호를 연결하고 최종 `MERGED` 상태를 확인합니다.

<a id="submission"></a>

## 6. 제출 정리 담당자: 실제 링크와 증빙 수집

**시작 조건:** A1~D2가 모두 병합되어 있어야 합니다. 전원 본인 PR 2개·타인 리뷰 2개·리뷰 수정 반영 1회를 확인합니다.
팀원은 본인 PR·Issue·리뷰 스레드·반영 커밋 URL을 담당자에게 전달합니다.

```sh
gh pr list --state merged --limit 100 --json number,title,author,url,mergedAt
```

목록만으로 리뷰 품질과 반영 여부는 판정할 수 없습니다. 각 PR의 실제 대화·커밋도 확인합니다.
작업 트리가 깨끗하면 최신 main을 받습니다.

```sh
git status --short
git switch main
git pull --ff-only origin main
python3 src/common.py "  Hello   Team  "
python3 src/1_upper.py
python3 src/2_lower.py
python3 src/3_length.py
python3 src/4_words.py
```

**확인:** `Hello Team`, `HELLO TEAM`, `hello team`, `10`, `2`가 순서대로 나와야 합니다.
파일이 누락되었거나 예상과 다른 출력이 있으면 제출 전에 해당 담당자가 고칩니다.

### 6-1. 제출 Issue와 브랜치

```sh
task_title='docs: collect collaboration evidence'
issue_body=$(mktemp)
cat > "$issue_body" <<'ISSUE'
## 목적
팀원별 기여 링크, 실제 Git 실습 기록, 최종 실행 결과와 히스토리를 제출 문서에 모은다.

## 완료 기준
- 전원 병합 PR 2개, 타인 리뷰 2개, 리뷰 수정 반영 1회 이상을 확인한다.
- 충돌 2회와 트러블슈팅 4종의 실제 기록을 확인한다.
- 실행 결과와 보호 규칙 증빙을 수집하고 체크리스트를 대조한다.
ISSUE
task_issue_url=$(gh issue create --title "$task_title" --assignee @me --body-file "$issue_body")
task_issue_number=${task_issue_url##*/}
printf '%s\n' "$task_issue_url"
git switch -c feature/submission-evidence
mkdir -p docs/evidence
```

### 6-2. 히스토리와 실제 출력 저장

```sh
git log --oneline --graph --all --decorate > docs/evidence/git-log.txt
python3 - <<'PY'
from pathlib import Path

path = Path("docs/evidence/git-log.txt")
path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")
PY
python3 --version > docs/evidence/execution-results.txt 2>&1
git rev-parse HEAD >> docs/evidence/execution-results.txt
printf '\nCommand: python3 src/common.py "  Hello   Team  "\nExpected: Hello Team\n' >> docs/evidence/execution-results.txt
python3 src/common.py "  Hello   Team  " >> docs/evidence/execution-results.txt 2>&1
printf '\nExpected for 1/2/3/4: HELLO TEAM / hello team / 10 / 2\n' >> docs/evidence/execution-results.txt
for task_script in src/1_upper.py src/2_lower.py src/3_length.py src/4_words.py; do
    printf '\nCommand: python3 %s\n' "$task_script"
    python3 "$task_script"
    task_exit_code=$?
    printf 'Exit code: %s\n' "$task_exit_code"
done >> docs/evidence/execution-results.txt 2>&1
cat docs/evidence/execution-results.txt
```

종료 코드·출력이 예상과 맞는지 직접 확인합니다. 파일이 생긴 것만으로 성공 처리하지 않습니다.
히스토리 저장 직후의 Python 명령은 그래프 출력의 줄 끝 공백만 제거합니다. 그대로 커밋하면 `git diff --cached --check`에서 공백 오류가 날 수 있습니다.
첫 PR에서 확인했던 빈 입력·한글 입력도 최신 코드에서 같은 방법으로 재확인하고 입력·명령·실제 결과를 덧붙입니다.
실행 날짜와 기준 SHA를 SUBMISSION.md에 적고, 보호 규칙 화면을 `docs/evidence/branch-protection.png`로 저장합니다.
히스토리 스냅샷에는 이후 생성하는 제출 정리 커밋 자체가 포함되지 않습니다.

### 6-3. 링크 확인 → 제출 PR

```sh
nano SUBMISSION.md docs/evidence/execution-results.txt
```

SUBMISSION.md에 전원의 실제 URL을 채웁니다. 실제로 충족한 항목만 체크합니다.
충돌·트러블슈팅 기록이 미기입이면 각 담당자가 먼저 완성하도록 합니다.

```sh
git add SUBMISSION.md docs/evidence
git diff --cached --stat
git diff --cached --check
git commit -m "docs: collect team contribution and execution evidence"
git push -u origin HEAD
```

[3~4단계](#pr-cycle)로 제출 PR에도 실질 리뷰·작성자 응답·승인을 남겨 병합합니다.
그 뒤 최종 PR URL·병합 SHA를 실제 제출 화면에 함께 기재합니다.

<a id="extra"></a>

## 7. 추가 상황: 필요할 때만 진행

아래는 필수 PR 2개씩을 만드는 단계와 별개입니다. 실제 문제가 발생했을 때만 실행합니다.

### 7-1. main에 긴급 수정이 필요한 경우

예: 완성된 단어 수 함수에서 실제로 빈 입력 오류가 발견된 경우입니다. 실습을 위해 일부러 오류를 넣지 않습니다.
깨끗한 작업 트리에서 시작합니다.

```sh
git fetch origin
git switch -c feature/hotfix-word-count origin/main
task_file='src/4_words.py'
task_title='fix: handle empty input in word count'
issue_body=$(mktemp)
nano "$issue_body"
```

Issue 본문에 재현 입력·실제 결과·기대 결과를 적습니다.

```sh
task_issue_url=$(gh issue create --title "$task_title" --assignee @me --body-file "$issue_body")
task_issue_number=${task_issue_url##*/}
printf '%s\n' "$task_issue_url"
nano "$task_file"
python3 "$task_file"
```

파일 하단 입력을 빈 문자열로 바꿔 재현·수정 전후 결과를 확인하고, 정상 입력도 확인한 뒤 예시 입력은 복원합니다.

```sh
git add "$task_file"
git diff --cached --check
git commit -m "$task_title"
git push -u origin HEAD
```

[3~4단계](#pr-cycle)로 긴급도를 알리고 빠르게 타인 리뷰를 받습니다. 보호 규칙은 우회하지 않습니다.
병합 후 main을 갱신해 다시 실행합니다. 이 프로젝트는 별도 서비스 배포 없이 실행·공유로 마무리합니다.

### 7-2. 의미 없는 커밋 메시지를 이미 push한 경우

공유 이력을 바로 재작성하지 않고 먼저 현재 내용을 확인합니다.

```sh
git fetch origin
git log --oneline origin/main..HEAD
gh pr view --json url,title,body
gh pr diff
```

현재 브랜치의 PR 설명에 기존 커밋이 무엇을 바꿨는지 보완합니다.

```sh
pr_body=$(mktemp)
gh pr view --json body --jq .body > "$pr_body"
nano "$pr_body"
gh pr edit --body-file "$pr_body"
```

이후 실제 변경부터 구체적인 메시지를 사용합니다. 설명 보완이 과거의 나쁜 메시지를 없애지는 않습니다.
아직 push하지 않은 최근 커밋이라면 A의 amend 절차를 사용할 수 있습니다. 공유된 브랜치는 팀 합의 없이 강제 push하지 않습니다.

### 7-3. README의 같은 구간에서 충돌이 반복되는 경우

```sh
git fetch origin
git log --oneline --all -- README.md
git blame README.md
git diff HEAD...origin/main -- README.md
```

누가 어떤 구간을 바꿨는지, 오래된 기준에서 작업했는지, PR 범위가 너무 큰지 확인합니다.
편집 구간을 나누고 PR을 작게 유지하며 제출 링크는 한 명이 취합합니다. 공통 코드 변경은 미리 알립니다.
일상 작업의 main 동기화는 작업을 커밋하거나 보관해 깨끗해진 feature 브랜치에서 진행합니다.

```sh
git merge origin/main
```

충돌하면 B·D와 같은 확인·합의·수정·`git add`·검증·커밋 순서로 해결합니다.
의도적인 충돌 실습 중에는 지정된 대기 시점을 지켜 재현 조건을 유지합니다.

## 명령 참고

- [GitHub CLI Issue 생성](https://cli.github.com/manual/gh_issue_create)
- [GitHub CLI PR 생성](https://cli.github.com/manual/gh_pr_create)
- [GitHub CLI 리뷰](https://cli.github.com/manual/gh_pr_review)
- [GitHub CLI PR 병합](https://cli.github.com/manual/gh_pr_merge)
- [체크리스트 모범 답안](B2-2-checklist-answer.md): 각 절차를 선택한 이유와 설명 예시
