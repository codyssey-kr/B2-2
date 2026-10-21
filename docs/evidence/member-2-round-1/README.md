# 팀원 2 · 1차 충돌 해결 증빙

- 참여자: `YeonJin` (`duswls98952`)
- 당시 작업 브랜치: `feature/2-round-1-heoney`
- PR: [#24](https://github.com/codyssey-kr/B2-2/pull/24)
- 대상: [2/length.py](../../../2/length.py), [src/common.py](../../../src/common.py)
- 기존 기록: [충돌 해결 기록의 팀원 2 · 1차](../../conflict-resolution.md)
- 해결 커밋: [1aae7aa](https://github.com/codyssey-kr/B2-2/commit/1aae7aaed69bcedc64980fa0079e3b0bac63fd1c)

## 증빙의 출처

1차 실습 당시 병합 터미널 출력은 보관되지 않았습니다. [conflict.json](conflict.json)은
2026-10-21에 별도 임시 저장소에서 해결 커밋의 두 부모를 다시 병합하며 수집한 결과입니다.
따라서 당시 실행 출력으로 표시하지 않았습니다. [validation.json](validation.json)은
같은 날 현재 `2/length.py`를 다시 실행해 확인한 결과입니다.

## 충돌 재현과 해결

해결 커밋 `1aae7aa`의 첫 번째 부모는 작업 커밋 `2055c61`, 두 번째 부모는
당시 병합 대상 `main`의 커밋 `72e83aa`입니다. 작업 커밋을 체크아웃한 임시 저장소에서
다음 명령을 실행했습니다. 기존 작업 브랜치는 변경하지 않았습니다.

```sh
git merge --no-commit 72e83aa9ddf65b32be69e402b6baa9d6aa56a482
```

재현 명령은 종료 코드 `1`과 다음 출력을 반환했습니다.

```text
Auto-merging 2/length.py
CONFLICT (content): Merge conflict in 2/length.py
Auto-merging docs/conflict-practice.md
Automatic merge failed; fix conflicts and then commit the result.
```

재현한 `2/length.py`의 충돌 부분은 다음과 같습니다. 전체 파일은 `conflict.json`에 있습니다.

> ```python
> <<<<<<< HEAD
>     text = text.strip()
> =======
>     text = normalize_spaces(text)
> >>>>>>> 72e83aa9ddf65b32be69e402b6baa9d6aa56a482
> ```

최종 해결 코드는 해결 커밋과 현재 파일에서 확인했습니다.

```python
    text = normalize_spaces(text)
    return len(text)
```

`strip()`은 앞뒤 공백만 제거하지만 `normalize_spaces()`는 내부 연속 공백과 탭·줄바꿈도
한 칸으로 정리합니다. 이 함수는 정리된 문자열의 길이를 그대로 세므로 구현 차이가
실제 결과에 나타납니다. 팀의 공통 공백 처리 기준에 맞춰 `normalize_spaces()`를 선택했습니다.

## 현재 검증과 병합 전후 비교

저장소 최상위에서 현재 파일을 실행한 명령과 실제 출력입니다. 실행 당시 `2/length.py`는
`origin/main`의 `7f5859f`와 같았습니다.

```sh
PYTHONPATH=. python3 2/length.py
```

```text
10
```

병합 전 코드는 `git show 2055c61:2/length.py`에서 읽어 실행했고, 해결 후 코드는
현재 `2/length.py`에서 읽어 실행했습니다. 아래는 이 문서 작성 시의 실제 결과입니다.

| 입력 | 병합 전 `strip()` | 해결 후 `normalize_spaces()` |
|---|---:|---:|
| `"  Hello   Team  "` | 12 | 10 |
| `" a\tB\nc "` | 5 | 5 |
| `""` | 0 | 0 |
| `" \t\n "` | 0 | 0 |
| `" 안녕  팀 "` | 5 | 4 |

재현 명령:

```sh
PYTHONPATH=. python3 - <<'PY'
import runpy
import subprocess

source = subprocess.check_output(['git', 'show', '2055c61:2/length.py'], text=True)
before_scope = {'__name__': 'before_replay'}
exec(compile(source, '2055c61:2/length.py', 'exec'), before_scope)
before = before_scope['count_characters']
after = runpy.run_path('2/length.py')['count_characters']
for value in ['  Hello   Team  ', ' a\tB\nc ', '', ' \t\n ', ' 안녕  팀 ']:
    print(f'{value!r}: before={before(value)}, after={after(value)}')
PY
```

이 표는 현재 재실행한 비교이며, 1차 실습 당시의 테스트 출력으로 소급하지 않습니다.
