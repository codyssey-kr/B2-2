# 4번 · 1차 충돌 해결 사례

## 1. 작업 정보

- **참여 계정:** `sohye-pk`
- **Issue:** [#17](https://github.com/codyssey-kr/B2-2/issues/17)
- **Pull Request:** [#28](https://github.com/codyssey-kr/B2-2/pull/28)
- **작업 브랜치:** `feature/4-round-1-sohye`
- **기준 커밋:** `de3995e6c92f58867291cf052dd04343a4b52887`
- **충돌 해결 대상 파일:** `4/first.py`
- **최종 해결 커밋:** `a062580f3ce24c25a49b63195067806fc71f5d6c`

이번 작업에서는 `first_word()` 함수의 공백 처리 방식을 두고 발생한 충돌을 검토하고, 프로젝트의 공통 함수인 `normalize_spaces()`를 사용하는 방식으로 해결했다.

## 2. 충돌 상황

`4/first.py`의 `first_word()` 함수에서 문자열의 앞뒤 공백을 처리하는 방식이 서로 달랐다.

`text.strip()`은 문자열의 앞뒤 공백을 제거한다. 반면 `normalize_spaces()`는 앞뒤 공백을 제거하는 것뿐만 아니라 연속된 공백 문자도 하나의 공백으로 정리한다.

따라서 두 방식은 처리할 수 있는 범위가 다르므로, 단순히 한쪽 코드를 선택하기보다 함수의 요구사항과 기존 공통 함수의 역할을 함께 고려해야 했다.

## 3. 충돌 해결 판단

최종적으로 `normalize_spaces(text)`를 사용하는 방식을 선택했다.

`first_word()`는 문장의 첫 단어를 반환하는 함수이므로, 문자열에 여러 공백이나 탭, 줄바꿈이 포함되어 있어도 일관되게 처리할 필요가 있다.

`normalize_spaces()`는 내부에서 `text.split()`을 사용해 공백 문자를 기준으로 문자열을 나눈 뒤, `" ".join()`으로 하나의 공백을 사용해 다시 연결한다. 따라서 앞뒤 공백을 제거하고 연속된 공백 문자도 정리할 수 있다.

반면 `text.strip()`만 사용하면 문자열 내부의 연속된 공백은 정리되지 않는다. 이에 따라 `text.strip()`은 최종 코드에 반영하지 않고 `normalize_spaces(text)`를 유지했다.

## 4. 최종 코드

파일: `4/first.py`

```python
"""문장의 첫 단어를 반환한다."""

from src.common import normalize_spaces


def first_word(text: str) -> str:
    """문장의 첫 단어를 반환한다. 빈 입력은 빈 문자열을 반환한다."""
    text = normalize_spaces(text)
    return text.split(" ")[0]


if __name__ == "__main__":
    print(first_word("  Hello   Team  "))  # 공백 정리 완료 후 예상: Hello
```

## 5. 검증 항목

다음 입력을 기준으로 공백 처리와 첫 단어 반환 결과를 확인할 수 있다.

| 입력값 | 예상 결과 | 확인할 내용 |
|---|---|---|
| `"  Hello   Team  "` | `"Hello"` | 앞뒤 공백 및 연속된 공백 처리 |
| `" a\tB\nc "` | `"a"` | 탭과 줄바꿈 처리 |
| `""` | `""` | 빈 문자열 처리 |
| `" \t\n "` | `""` | 공백 문자만 있는 입력 처리 |
| `" 안녕  팀 "` | `"안녕"` | 한글 입력 및 연속된 공백 처리 |

위 결과는 코드의 동작 방식에 따른 예상 결과이며, 실제 실행 결과와 종료 코드는 테스트를 실행한 뒤 기록해야 한다.

### 실행 명령어

프로젝트 루트 디렉터리에서 다음 명령어로 실행할 수 있다.

```bash
PYTHONPATH=. python3 4/first.py
```

예상 출력:

```text
Hello
```

- **실제 실행 결과:** `Hello`
- **종료 코드:** `0`

## 6. 자체 검토

- `first_word()`가 공백 정리 후 첫 단어를 반환하도록 구성했다.
- `normalize_spaces()`를 사용해 앞뒤 공백뿐 아니라 연속된 공백 문자도 처리하도록 했다.
- 빈 문자열과 공백 문자만 포함된 입력에서 빈 문자열을 반환하는지 확인할 수 있도록 검증 항목을 정리했다.
- 최종 선택은 `normalize_spaces(text)`이며, `text.strip()`은 최종 코드에 반영하지 않았다.
- Pull Request 설명에도 실제 최종 코드와 일치하도록 해결 방식을 명확하게 기록해야 한다.

## 7. 재현 및 변경 사항 확인

아래는 원본 브랜치 feature/4-round-1의 내용을 기준으로 재현용 브랜치를 생성한 뒤, main 브랜치의 변경 사항을 병합하여 충돌을 확인하는 방법이다.

```bash
git switch feature/4-round-1
git switch -c conflict-replay
git merge --no-commit main
git status
git diff -- 4/first.py
```

충돌이 발생하면 git status로 충돌 파일을 확인하고, git diff -- 4/first.py로 해당 파일의 변경 내용을 확인한다.

재현용 병합을 취소하려면 다음 명령어를 실행한다.

```bash
git merge --abort
```

재현이 끝난 뒤에는 원본 브랜치로 돌아갈 수 있다.

```bash
git switch feature/4-round-1
```

참고: 위 명령은 로컬 main 브랜치를 병합 대상으로 사용한다. 실제 충돌 발생 여부는 두 브랜치의 현재 상태에 따라 달라질 수 있다.
