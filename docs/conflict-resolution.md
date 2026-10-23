# 충돌 해결 기록

실제로 수행한 뒤 채웁니다. 빈 양식은 완료 증빙이 아닙니다.
최신 main을 병합한 뒤 자기 차수의 기록을 작성하고 다른 사람의 기록을 유지합니다.

## 팀원 1 · 1차

- 참여자와 역할: `parkhojeong`의 해결·셀프리뷰 사례. Codex가 요청에 따라 명령과 검증을 실행했습니다.
- 브랜치·파일: `feature/1-round-1`, `1/upper.py`.
- 기준 커밋: 작업 `8395187`, main `bb5ebb7`.
- 양쪽 코드: `text.strip()`과 `normalize_spaces(text)`가 같은 줄에서 충돌했습니다.
- 해결 이유: 내부 연속 공백과 탭·줄바꿈까지 정리해야 하므로 공통 함수를 선택했습니다.
- 검증: 정상·경계 입력 5개 및 파일 직접 실행 통과.
- PR: [#12](https://github.com/codyssey-kr/B2-2/pull/12).
- 원문 로그·충돌 마커·전후 결과·재현 명령: [해결 사례](evidence/member-1-round-1/README.md).
- 배운 점: 어느 쪽 코드를 선택할지 요구사항과 실제 출력으로 판단합니다. 타인의 승인 리뷰는 별도입니다.

## 팀원 1 · 2차

- 참여자: `parkhojeong`; 요청에 따라 Codex가 실제 명령과 검증을 실행했습니다.
- 브랜치·파일: `feature/1-round-2`, `1/lower.py`.
- 기준 커밋: 작업 `d1e7c9c`, main `aa2d9f6`.
- 충돌: `text.strip()`과 `normalize_spaces(text)`가 같은 줄을 수정했습니다.
- 해결 이유: 내부 연속 공백·탭·줄바꿈까지 정리하기 위해 공통 함수를 선택했습니다.
- 검증: 정상·경계 입력 5개와 파일 직접 실행 통과.
- PR: [#20](https://github.com/codyssey-kr/B2-2/pull/20).
- 원문 증빙·전후 결과·재현 명령: [2차 해결 사례](evidence/member-1-round-2/README.md).
- 자기 점검 기록이며 타인의 승인 리뷰는 별도입니다.

## 팀원 2 · 1차


- 참여자와 역할: `YeonJin`; 팀원 2의 글자 수 계산 함수 충돌 해결 및 검증을 수행했습니다.
- 브랜치·기준 커밋·파일: `feature/2-round-1-heoney`, 작업 `2055c61`, 공통 기준 `2e3f879`, `2/length.py`.
- 양쪽 코드와 충돌 마커: `text.strip()`과 `normalize_spaces(text)`가 같은 줄에서 충돌했습니다. `>>>>>> main`을 확인했습니다.
- 공백 처리 방식 비교와 합의한 해결 이유: `text.strip()`은 앞뒤 공백만 제거하지만, `normalize_spaces(text)`는 내부 연속 공백과 탭·줄바꿈까지 정리하므로 `main`의 요구사항에 맞춰 공통 함수를 선택했습니다.
- 실행 명령·입력·예상 결과·실제 결과: `PYTHONPATH=. python3 2/length.py` 실행 시 예상·실제 `10`. `" a\tB\nc "`은 `5`, `""`와 `" \t\n "`은 각각 `0`으로 예상·실제 결과가 일치했습니다.
- PR·해결 커밋 링크: [PR #24](https://github.com/codyssey-kr/B2-2/pull/24), [해결 커밋 1aae7aa](https://github.com/duswls98952/B2-2-Practice/commit/1aae7aa).
- 배운 점과 예방 방법: 충돌한 코드의 동작을 비교하고 요구사항에 맞는 구현을 선택해야 합니다. 공통 함수 사용 기준을 팀 내에서 공유하면 유사한 충돌을 예방할 수 있습니다.

## 팀원 2 · 2차

- 참여자와 역할:
- 브랜치·기준 커밋·파일:
- 양쪽 코드와 충돌 마커:
- 공백 처리 방식 비교와 합의한 해결 이유:
- 실행 명령·입력·예상 결과·실제 결과:
- PR·해결 커밋 링크:
- 배운 점과 예방 방법:

## 팀원 3 · 1차

- 참여자와 역할: 최민채; 충돌 재현 및 해결, 공백 처리 방식 비교, 테스트 수행, 해결 과정 문서화
- 브랜치·기준 커밋·파일: 작업 브랜치: feature/3-round-1, 기준 커밋: [실제 병합 전 origin/main의 커밋 해시], 대상 파일: 3/reverse.py
- 양쪽 코드와 충돌 마커: main에서는 공백을 정규화하는 normalize_spaces(text)를 사용하도록 변경했고, 작업 브랜치에서는 문자열 양끝의 공백을 제거하는 text.strip()을 사용하도록 수정했다. 두 변경 사항이 같은 코드 영역에 적용되어 Git이 자동으로 병합하지 못하는 상황이 발생했다.
- 공백 처리 방식 비교와 합의한 해결 이유: 프로젝트의 공통 함수인 normalize_spaces(text)를 활용하면 공백 처리 규칙을 여러 곳에서 중복 구현하지 않고 일관되게 유지할 수 있다. 또한 기존의 단어 분리 및 순서 뒤집기 기능을 유지하면서 정상 입력과 경계 입력을 동일한 기준으로 처리할 수 있다.
- 실행 명령·입력·예상 결과·실제 결과: 최종 구현은 실제 코드와 팀의 합의 내용을 확인한 후 확정한다. 저장소 최상위 폴더에서 실행한다.
- PR·해결 커밋 링크: 관련 Issue: [실제 Issue URL 및 번호]
PR: [실제 PR URL], 작성자 변경 커밋: [실제 커밋 해시 또는 URL], 충돌 해결 커밋: [실제 커밋 해시 또는 URL], 문서 기록 커밋: [실제 커밋 해시 또는 URL], 리뷰어 및 승인 결과: [실제 리뷰어 이름과 승인 상태]
- 배운 점과 예방 방법: 같은 파일의 같은 부분을 여러 브랜치에서 수정하면 Git이 자동으로 병합하지 못할 수 있다.
충돌을 해결할 때는 충돌 마커만 제거하지 말고 양쪽 코드의 목적과 기능 차이를 비교해야 한다.
text.strip()과 normalize_spaces(text)는 처리 범위가 다르므로 요구사항에 맞는 방식을 선택해야 한다.
공통 공백 처리 함수를 사용하면 코드 중복을 줄이고 팀 전체의 처리 규칙을 통일할 수 있다.
git commit --amend --reset-author --no-edit는 최신 커밋의 작성자를 변경하고 커밋 해시를 바꾸므로, 공유 브랜치가 아닌 본인 소유의 작업 브랜치에서만 신중하게 사용해야 한다.
충돌 해결 후에는 git diff --check, 프로그램 실행, 정상 입력 및 경계 입력 테스트를 수행해야 한다.
PR 리뷰 의견에 답변하고 필요한 수정을 반영한 뒤, 작성자 외 팀원 1명 이상의 승인을 받고 병합해야 한다.
작업 결과와 실제 검증 내용을 docs/conflict-resolution.md에 기록해 이후 충돌 해결 시 참고할 수 있도록 한다.

## 팀원 3 · 2차

- 참여자와 역할: 최민채; 3/exclaim.py의 공백 처리 충돌 해결, 입력별 테스트, Git revert 실습 및 결과 문서화를 수행했습니다.
- 브랜치·기준 커밋·파일: 충돌 해결 작업 브랜치 feature/3-round-2, 기준 브랜치 origin/main, 충돌 해결 커밋 4ed3463, 대상 파일 3/exclaim.py. revert 실습은 별도 브랜치 feature/3-round-2-retry에서 수행했습니다.
- 양쪽 코드와 충돌 마커: 작업 브랜치에서는 text = text.strip()을 사용했고, main에서는 text = normalize_spaces(text)를 사용했습니다. 두 변경 사항이 같은 코드 영역에 적용되어 <<<<<<< HEAD, =======, >>>>>>> origin/main 충돌 마커가 발생했습니다.
- 공백 처리 방식 비교와 해결 이유: text.strip()은 문자열 앞뒤의 공백을 제거하지만 내부의 연속 공백은 정리하지 않습니다. normalize_spaces(text)는 앞뒤 공백을 제거하고 내부 연속 공백, 탭 및 줄바꿈을 정리합니다. 프로젝트의 공통 공백 처리 규칙을 따르기 위해 normalize_spaces(text)를 선택했습니다.
- 실행 명령·입력·예상 결과·실제 결과:
실행 명령: PYTHONPATH=. python3 3/exclaim.py
예상 출력: Hello Team!
일반 입력 " Hello Team " → "Hello Team!"
입력 " a\tB\nc " → "a B c!"
빈 입력 "" → ''
공백 입력 " \t\n " → ''
실제 결과는 예상 결과와 일치했습니다.
- PR·해결 커밋 링크:
PR: #32 — 충돌 해결 및 revert 실습
충돌 해결 커밋: 4ed3463
- 배운 점과 예방 방법: 같은 줄을 서로 다른 방식으로 수정하면 병합 충돌이 발생할 수 있습니다. 각 구현의 동작과 요구사항을 비교하고, 충돌 해결 후 정상 입력과 경계 입력을 모두 테스트해야 합니다. 공통 함수를 재사용하면 공백 처리 규칙을 일관되게 유지할 수 있습니다.
- 추가 실습: Git revert
- 참여자: 최민채.
- 상황·기준 브랜치: feature/3-round-2-retry에서 기존 충돌 해결 결과를 유지한 채 별도의 실습용 변경을 만들었습니다. 실습 시작 당시 기준 커밋은 0bb0a08이었습니다.
- 원격에 push한 대상 실습 커밋: d11eb50 — test: add revert practice change for exclaim.
- 실제 명령:
git status
git diff --check
git diff -- 3/exclaim.py
PYTHONPATH=. python3 3/exclaim.py
git add 3/exclaim.py
git commit -m "test: add revert practice change for exclaim"
git push origin feature/3-round-2-retry
git revert --no-edit d11eb50
git log --oneline -5
git diff HEAD^ HEAD -- 3/exclaim.py
git push origin feature/3-round-2-retry
- 새로 생긴 revert 커밋과 되돌린 파일: a8bf854. 3/exclaim.py에서 text = text.strip() 변경을 취소하고 text = normalize_spaces(text)로 복구했습니다.
- 기존 이력이 보존되었음을 확인한 결과: git log --oneline -5에서 실습용 커밋 d11eb50과 revert 커밋 a8bf854가 모두 남아 있음을 확인했습니다. 두 커밋은 원격 브랜치 origin/feature/3-round-2-retry에도 push했습니다.
- revert 후 검증 명령·입력·예상 결과·실제 결과:
PYTHONPATH=. python3 3/exclaim.py → Hello Team!
일반 입력 " Hello Team " → 'Hello Team!'
빈 입력 "" → ''
공백 입력 " " → ''
탭 입력 "\tHello\t" → 'Hello!'
줄바꿈 입력 "\nHello\n" → 'Hello!'
다섯 가지 입력 테스트가 모두 예상 결과와 일치했습니다.
- 주의점과 reset 대신 선택한 이유: git revert는 기존 커밋을 삭제하거나 브랜치 이력을 재작성하지 않고, 변경 사항을 취소하는 새 커밋을 생성합니다. 이미 원격에 push한 변경을 취소하면서 이력을 보존하기 위해 git reset 대신 git revert를 선택했습니다.
- PR·커밋·증빙 링크:
PR: #32 — 충돌 해결 및 revert 실습
충돌 해결 커밋: 4ed3463
실습용 커밋: d11eb50
revert 커밋: a8bf854
로컬 증빙 폴더: evidence/revert-practice/
캡처 파일명은 실제 파일 목록을 확인한 후 최종 기록합니다.
- 배운 점과 예방 방법: 이미 원격에 push한 커밋을 취소할 때 git revert를 사용하면 기존 이력을 보존하면서 취소 내역을 남길 수 있습니다. 실습 결과와 실제 명령 출력, 테스트 결과 및 증빙을 함께 기록하면 이후 같은 문제를 재현하고 검토하기 쉽습니다.

## 팀원 4 · 1차

- 참여자와 역할:
- 브랜치·기준 커밋·파일:
- 양쪽 코드와 충돌 마커:
- 공백 처리 방식 비교와 합의한 해결 이유:
- 실행 명령·입력·예상 결과·실제 결과:
- PR·해결 커밋 링크:
- 배운 점과 예방 방법:

## 팀원 4 · 2차

- 참여자와 역할:
- 브랜치·기준 커밋·파일:
- 양쪽 코드와 충돌 마커:
- 공백 처리 방식 비교와 합의한 해결 이유:
- 실행 명령·입력·예상 결과·실제 결과:
- PR·해결 커밋 링크:
- 배운 점과 예방 방법:
