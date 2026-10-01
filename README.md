# B2-2 · Team Utils

4명이 공통 공백 정리 유틸을 사용하는 간단한 함수를 만들며 Git 협업을 연습합니다.

**팀원은 [전체 실습 시나리오와 명령어](reference/B2-2-scenarios.md)를 순서대로 따라 하세요.**
현재는 오류 수정 실습용 준비본입니다. `src/common.py`는 정상 구현이며, `src/1_upper.py`~`src/4_words.py`에는 의도적인 오류가 있습니다.
각자 feature 브랜치에서 담당 파일을 바로 고친 뒤 PR로 병합합니다.

## 공통 함수 실행

Python 3.10 이상에서, 저장소 루트에서 실행합니다. 별도 패키지 설치는 필요 없습니다.

```sh
python3 src/common.py "  Hello   team!  "
```

예상 출력은 `Hello team!`입니다.

<a id="tasks"></a>

## 팀원별 과제

| 역할 | 수정할 파일 | 함수 / 수정 힌트 | Issue 제목 |
| --- | --- | --- | --- |
| A | [1_upper.py](src/1_upper.py) | `to_upper` / `upper()` | `feat: 대문자 변환 함수 구현` |
| B | [2_lower.py](src/2_lower.py) | `to_lower` / `lower()` | `feat: 소문자 변환 함수 구현` |
| C | [3_length.py](src/3_length.py) | `count_characters` / `len()` | `feat: 글자 수 계산 함수 구현` |
| D | [4_words.py](src/4_words.py) | `count_words` / `split()` 후 `len()` | `feat: 단어 수 계산 함수 구현` |

초안은 함수 본문까지 구현되어 있지만 일부 결과가 틀립니다. 공통 함수 호출은 유지하고, 아래 예상 결과와 비교해 잘못된 반환식을 수정합니다.
현재 잘못된 결과는 A `Hello team`, B `HELLO TEAM`, C `9`이며, D는 빈 입력을 `1`로 셉니다.
별도 테스트 코드는 만들지 않고 사용 예시를 직접 실행해 확인합니다.

<a id="examples"></a>

## 수정 후 실행 예시

| 역할 | 명령 | 기본 입력 `"  Hello   Team  "`의 예상 출력 |
| --- | --- | --- |
| A | `python3 src/1_upper.py` | `HELLO TEAM` |
| B | `python3 src/2_lower.py` | `hello team` |
| C | `python3 src/3_length.py` | `10` — 정리된 중간 공백 1개 포함 |
| D | `python3 src/4_words.py` | `2` |

위 결과는 각 담당자가 오류를 고친 뒤의 기준입니다. 파일 하단의 입력을 바꿔 아래 결과도 직접 확인한 뒤 원래 입력으로 복원합니다.

| 입력 | A: 대문자 | B: 소문자 | C: 글자 수 | D: 단어 수 |
| --- | --- | --- | --- | --- |
| `""` | 빈 줄 | 빈 줄 | `0` | `0` |
| `"   "` | 빈 줄 | 빈 줄 | `0` | `0` |
| `"안녕 팀원들"` | `안녕 팀원들` | `안녕 팀원들` | `6` | `2` |

## 문서

| 문서 | 용도 |
| --- | --- |
| [실습 시나리오](reference/B2-2-scenarios.md) | 준비부터 Issue·PR·리뷰·Git 실습·제출까지 순서와 명령 |
| [모범 답안](reference/B2-2-checklist-answer.md) | 필수 체크리스트 21개 항목의 설명·증빙 예시 |
| [미션 원문](reference/B2-2.md) · [체크리스트](reference/B2-2-checklist.md) | 공식 요구사항 확인 |
| [협업 규칙](docs/CONTRIBUTING.md) | 팀 브랜치·커밋·PR·리뷰 규칙 |
| [충돌 기록](docs/conflict-resolution.md) · [Git 실습 기록](docs/troubleshooting-log.md) | 실제 수행 후 작성 |
| [제출물 인덱스](SUBMISSION.md) | 실제 기여·증빙 링크 모음 |
