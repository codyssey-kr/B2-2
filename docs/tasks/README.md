# 작업 참고 자료

1번은 `parkhojeong`의 [충돌 해결·셀프리뷰 사례](../evidence/member-1-round-1/README.md)입니다.
나머지 세 명은 2·3·4번을 맡습니다. 자기 점검과 타인의 승인 리뷰는 구분합니다.

팀원은 각자 브랜치의 참고 문서를 읽고 Issue를 직접 작성합니다.
아래 경로는 해당 작업 브랜치에 있으며, PR 병합 후 main에도 모입니다.

| 팀원 | 차수 | 브랜치 | 참고 문서 |
|---|---|---|---|
| 1 | 1차 | `feature/1-round-1` | `docs/tasks/1-round-1.md` |
| 1 | 2차 | `feature/1-round-2` | `docs/tasks/1-round-2.md` |
| 2 | 1차 | `feature/2-round-1` | `docs/tasks/2-round-1.md` |
| 2 | 2차 | `feature/2-round-2` | `docs/tasks/2-round-2.md` |
| 3 | 1차 | `feature/3-round-1` | `docs/tasks/3-round-1.md` |
| 3 | 2차 | `feature/3-round-2` | `docs/tasks/3-round-2.md` |
| 4 | 1차 | `feature/4-round-1` | `docs/tasks/4-round-1.md` |
| 4 | 2차 | `feature/4-round-2` | `docs/tasks/4-round-2.md` |

기준 구현과 1번 사례를 먼저 main에 반영한 뒤 2·3·4번이 순서대로 실습합니다.
4번도 두 개의 파일과 두 차례 작업 브랜치를 사용합니다.

전체 진행 순서는 [실습 안내](../conflict-practice.md)를 참고합니다.
이 문서와 브랜치 준비만으로 Issue 작성이나 평가용 기여가 완료되는 것은 아닙니다.

## 2차 트러블슈팅 분담

| 담당 | 코드 실습 | Git 실습 |
|---|---|---|
| 1번 | 소문자 변환 충돌 해결 | amend — [실제 수행 사례](../evidence/member-1-round-2/README.md) |
| 2번 | 단어 수 계산 충돌 해결 | reset --soft |
| 3번 | 느낌표 붙이기 충돌 해결 | revert |
| 4번 | 마지막 단어 찾기 충돌 해결 | stash / stash pop |

2·3·4번은 먼저 자신의 1차 작업을 마치고 준비된 2차 브랜치를 사용합니다.
각자 2차 Issue를 직접 작성해 Draft PR에 연결하고, 충돌 해결을 커밋한 다음 Git 실습을 진행합니다.
자기 실습 과정은 `docs/troubleshooting-log.md`의 담당 항목에 작성합니다.
1번 기록 외의 빈 양식은 수행 완료 증빙이 아닙니다.
