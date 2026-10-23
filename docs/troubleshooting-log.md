# Git 트러블슈팅 기록

실제 수행 후 참여자·상황·명령·전후 결과·주의점·PR/커밋 링크를 기록합니다.
안내나 빈 양식만 있는 항목은 수행 완료가 아닙니다.

| 담당 | 실습 | 상태 |
|---|---|---|
| 1번 (`parkhojeong`) | amend | 완료 — 원문 증빙 포함 |
| 2번 | reset --soft | 미수행 — 담당자가 직접 진행 |
| 3번 | revert | 미수행 — 담당자가 직접 진행 |
| 4번 | stash / stash pop | 미수행 — 담당자가 직접 진행 |

## 1번: amend

- 참여자: `parkhojeong`; Codex가 요청에 따라 실제 명령을 실행했습니다.
- 상황: `feature/1-round-2`의 아직 push하지 않은 최근 문서 커밋 메시지를 구체화했습니다.
- 변경 전: `3e18bcce9798fa358f07d8fd9430e7f276f77293` — `docs: add troubleshooting log`.
- 명령: `git commit --amend -m "docs: prepare participant troubleshooting assignments"`.
- 변경 후: `b41b7b526a1adbd0a07b68b50851fc089c1509d2` — `docs: prepare participant troubleshooting assignments`.
- 결과: 커밋 ID와 메시지는 바뀌었고 부모 커밋과 파일 트리는 동일했습니다.
- 주의점: 공개 전 로컬 커밋에만 적용했습니다. 이전 커밋은 교체되었으므로 원문 증빙에 정보를 보관했습니다.
- 선택 이유: 파일 내용은 유지하고 최근 커밋 메시지만 구체적으로 수정하기 위해 amend를 사용했습니다.
- PR: [#20](https://github.com/codyssey-kr/B2-2/pull/20).
- [전후 커밋 정보와 실제 명령 출력](evidence/member-1-round-2/amend.json).

## 2번: reset --soft

- 참여자:
- 상황·기준 브랜치:
- 공개 전 커밋과 부모 커밋:
- 실제 명령:
- reset 후 HEAD·index·작업 파일 상태:
- 변경을 유지한 채 다시 커밋한 결과:
- 주의점과 선택 이유:
- PR·커밋·증빙 링크:

원격에 공개하지 않은 본인 실습 커밋으로만 수행합니다.

## 3번: revert
- 참여자: 최민채
- 상황·기준 브랜치: feature/3-round-2-retry. 기존 충돌 해결 결과를 유지한 상태에서 실습용 변경을 만들었습니다. 실습 시작 당시 기준 커밋은 0bb0a08이었습니다.
- 원격에 push한 대상 실습 커밋: d11eb50 — test: add revert practice change for exclaim
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
- 새로 생긴 revert 커밋과 되돌린 파일: a8bf854. 3/exclaim.py의 text = text.strip() 변경을 취소하고 text = normalize_spaces(text)로 복구했습니다.
- 기존 이력이 보존되었음을 확인한 결과: git log --oneline -5에서 실습용 커밋 d11eb50과 revert 커밋 a8bf854가 모두 남아 있음을 확인했습니다. 두 커밋은 원격 브랜치 origin/feature/3-round-2-retry에도 push했습니다.
검증 결과:
PYTHONPATH=. python3 3/exclaim.py → Hello Team!
일반 입력 " Hello Team " → 'Hello Team!'
빈 입력 "" → ''
공백 입력 " " → ''
탭 입력 "\tHello\t" → 'Hello!'
줄바꿈 입력 "\nHello\n" → 'Hello!'
다섯 가지 입력 테스트가 모두 예상 결과와 일치했습니다.
- 주의점과 reset 대신 선택한 이유: git revert는 기존 커밋을 삭제하지 않고 변경 사항을 취소하는 새 커밋을 생성합니다. 이미 원격에 push한 커밋을 되돌리면서 기존 이력을 보존하기 위해 git reset 대신 git revert를 선택했습니다.
- PR·커밋·증빙 링크:
PR: #32 — 충돌 해결 및 revert 실습
실습용 커밋: d11eb50
revert 커밋: a8bf854
로컬 증빙 폴더: evidence/revert-practice/
캡처 파일명은 실제 파일 목록을 확인한 후 최종 기록합니다.

원격에 공개하지 않은 본인 실습 커밋으로만 수행합니다.

## 4번: stash / stash pop

- 참여자:
- 상황·기준 브랜치:
- 보관 전 작업 파일·diff:
- 실제 명령과 stash 식별 정보:
- 보관 후 작업 트리·브랜치 전환 결과:
- 원래 브랜치 복귀·pop 후 복원된 diff:
- 주의점과 선택 이유:
- PR·커밋·증빙 링크:

충돌 해결을 먼저 커밋한 뒤 별도의 미커밋 변경으로 실습합니다.
