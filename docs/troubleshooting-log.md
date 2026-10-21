# Git 트러블슈팅 기록

실제 수행 후 참여자·상황·명령·전후 결과·주의점·PR/커밋 링크를 기록합니다.
안내나 빈 양식만 있는 항목은 수행 완료가 아닙니다.

| 담당 | 실습 | 상태 |
|---|---|---|
| 1번 (`parkhojeong`) | amend | 완료 — 원문 증빙 포함 |
| 2번 (`YeonJin`) | reset --soft | 완료 — reset 전후 결과 기록 |
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

- 참여자: `YeonJin`; `reset --soft`를 이용한 커밋 취소 및 변경 유지 실습을 수행했습니다.
- 상황·기준 브랜치: `feature/2-round-2-heoney`에서 충돌 해결 커밋 `0ed95d3`을 완료한 후 별도의 실습 파일을 생성했습니다.
- 공개 전 커밋과 부모 커밋: 실습 커밋 `26256ba`, 부모 커밋 `0ed95d3`.
- 실제 명령: `git commit -m "docs: add reset practice note"` → `git reset --soft HEAD~1` → `git status --short` → `git diff --cached -- docs/practice/member-2-reset.md` → `git commit -m "docs: retain reset practice changes"`.
- reset 후 HEAD·index·작업 파일 상태: HEAD는 `0ed95d3`으로 돌아갔고, index에는 `A  docs/practice/member-2-reset.md`가 표시됐습니다. 파일과 내용은 그대로 유지됐습니다.
- 변경을 유지한 채 다시 커밋한 결과: `a7b9a5d` 커밋으로 연습 파일을 다시 기록했습니다.
- 주의점과 선택 이유: `--soft`는 커밋 위치만 변경하고 index와 작업 파일을 유지합니다. 공유된 커밋 이력을 변경하지 않도록 Push 전에 별도 실습 커밋으로 진행했습니다.
- PR·커밋·증빙 링크: [PR #26](https://github.com/codyssey-kr/B2-2/pull/26), [재커밋 a7b9a5d](https://github.com/codyssey-kr/B2-2/commit/a7b9a5d210baab3ce1e6e47bfcfeb6a394527efa). `26256ba`는 reset으로 취소했으며, 실제 실행 결과는 위 항목에 기록했습니다.
- 당시 status·diff 출력과 사후 조회한 Reset 전후 HEAD: [팀원 2 · 2차 증빙](evidence/member-2-round-2/README.md).

원격에 공개하지 않은 본인 실습 커밋으로만 수행합니다.

## 3번: revert

- 참여자:
- 상황·기준 브랜치:
- 원격에 push한 대상 실습 커밋:
- 실제 명령:
- 새로 생긴 revert 커밋과 되돌린 파일:
- 기존 이력이 보존되었음을 확인한 결과:
- 주의점과 reset 대신 선택한 이유:
- PR·커밋·증빙 링크:

자신의 작업 브랜치에 올린 실습용 변경을 되돌립니다. main에 직접 push하지 않습니다.

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
