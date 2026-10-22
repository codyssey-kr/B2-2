# 팀원 2 · 2차 충돌 해결 및 Reset 증빙

- 참여자: `YeonJin` (`duswls98952`)
- 브랜치: `feature/2-round-2-heoney`
- Issue: [#25](https://github.com/codyssey-kr/B2-2/issues/25)
- PR: [#26](https://github.com/codyssey-kr/B2-2/pull/26)
- 대상 코드: [2/words.py](../../../2/words.py), [src/common.py](../../../src/common.py)
- 관련 기록: [충돌 해결 기록](../../conflict-resolution.md), [트러블슈팅 기록](../../troubleshooting-log.md)

구조화한 출력: [충돌 재현](conflict.json), [현재 코드 검증](validation.json),
[Reset 당시 기록과 사후 조회](reset.json). 각 JSON의 `source`에 출력의 출처를 적었습니다.

## 증빙의 출처

이 문서는 2026-10-21에 작성했습니다. 당시 실행 명령, 충돌 마커 및 Reset 직후의
`git status --short`·`git diff --cached` 출력은 사용자가 제공한 작업 인계 기록에서 옮겼습니다.
현재 코드의 테스트 출력과 Git 이력 조회 출력은 문서 작성 과정에서 Codex가 실제로 실행해 확인했습니다.
두 시점의 결과를 각 항목에 표시했습니다.

당시 병합 명령의 터미널 메시지 원문과 Reset 직후의 `git log -1` 출력은 인계 자료에 없습니다.
해당 출력은 복원하거나 추정하지 않았습니다. Reset 후 HEAD는 아래의 현재 reflog 조회로 확인했습니다.

## 충돌과 해결

### 당시 수행 내용 — 인계 기록

준비 커밋 `fbfddd4`에서 다음 명령을 실행했고, `2/words.py`의 공백 처리 줄에서 충돌을 확인했습니다.
병합 대상은 해결 커밋의 두 번째 부모인 `0f033fb`였습니다. 부모 정보는 아래 사후 조회 결과에 있습니다.

```sh
git merge origin/main
```

당시 터미널 메시지 원문은 미보관입니다. 인계 기록에 보관된 충돌 마커는 다음과 같습니다.

> ```python
> <<<<<<< HEAD
>     text = text.strip()
> =======
>     text = normalize_spaces(text)
> >>>>>>> origin/main
> ```

원문 메시지를 대신하지 않고, 동일한 두 커밋을 임시 로컬 저장소에서 다시 병합해 확인했습니다.
기존 작업 브랜치에는 영향을 주지 않았습니다. 재현 명령과 실제 결과는 [conflict.json](conflict.json)에
있습니다. 재현한 마커의 끝 표시는 명령에 사용한 커밋 해시이며, 위의 당시 기록은 `origin/main`입니다.

최종 해결 코드는 다음과 같으며, 문서 작성 시 현재 파일에서도 확인했습니다.

```python
    text = normalize_spaces(text)
    return len(text.split())
```

`strip()`은 앞뒤 공백만 제거합니다. 공통 함수 `normalize_spaces()`는
`" ".join(text.split())`으로 앞뒤 공백을 제거하고, 내부 연속 공백과 탭·줄바꿈을 한 칸으로 정리합니다.
이 함수에서는 뒤이어 호출하는 `split()` 때문에 두 방식의 단어 수가 같을 수 있습니다.
팀의 공통 공백 처리 기준을 따르기 위해 `normalize_spaces()`를 선택했습니다.

- [준비 커밋 fbfddd4](https://github.com/codyssey-kr/B2-2/commit/fbfddd49785fc2df9e8e8edc1c837870e6ce16dc)
- [충돌 해결 커밋 0ed95d3](https://github.com/codyssey-kr/B2-2/commit/0ed95d31981fd61625fb7e8ea1940e994c1a57e7)

### 현재 코드 검증 — 문서 작성 시 재실행

저장소 최상위에서 실행했습니다. 검증 당시 HEAD는 `42a7761`이며, 코드 파일의 미커밋 변경은 없었습니다.
아래는 과거 실행 로그가 아닌 이번 재실행의 실제 출력입니다.

기본 실행 명령:

```sh
PYTHONPATH=. python3 2/words.py
```

실제 출력(종료 코드 0):

```text
2
```

정상·경계 입력 검증 명령:

```sh
PYTHONPATH=. python3 - <<'PY'
import runpy

count_words = runpy.run_path('2/words.py')['count_words']
cases = [
    ('  Hello   Team  ', 2),
    (' a\tB\nc ', 3),
    ('', 0),
    (' \t\n ', 0),
]
for text, expected in cases:
    actual = count_words(text)
    print(f'{text!r}: expected={expected}, actual={actual}')
    assert actual == expected
print('PASS: 4/4')
PY
```

실제 출력(종료 코드 0):

```text
'  Hello   Team  ': expected=2, actual=2
' a\tB\nc ': expected=3, actual=3
'': expected=0, actual=0
' \t\n ': expected=0, actual=0
PASS: 4/4
```

## Reset 실습

### 목적과 당시 명령 — 인계 기록

충돌 해결 커밋을 보존한 상태에서 별도의 실습 커밋을 취소하고, 파일 변경은 스테이징된 상태로
유지되는지 확인했습니다. Push 전 실습 커밋 `26256ba`에 다음 명령을 실행했습니다.

```sh
git reset --soft HEAD~1
```

당시 상태 확인 명령:

```sh
git status --short
```

인계 기록에 보관된 실제 출력:

```text
A  docs/practice/member-2-reset.md
```

당시 스테이징 내용 확인 명령:

```sh
git diff --cached -- docs/practice/member-2-reset.md
```

인계 기록에 보관된 실제 출력:

```diff
diff --git a/docs/practice/member-2-reset.md b/docs/practice/member-2-reset.md
new file mode 100644
index 0000000..916ca36
--- /dev/null
+++ b/docs/practice/member-2-reset.md
@@ -0,0 +1 @@
+2번 reset 실습: 커밋 취소 후 변경 유지 확인
```

`--soft`는 HEAD를 이동시키고 index와 작업 트리를 유지합니다.
따라서 새 파일의 추가 내용은 스테이징된 상태로 남았으며, 다음 명령으로 재커밋했습니다.

```sh
git commit -m "docs: retain reset practice changes"
```

재커밋은 `a7b9a5d`입니다. 실습 파일은 이후 리뷰 반영 커밋 `42a7761`에서 삭제했습니다.
현재 문서는 당시 실습을 보관하는 기록이며, 파일을 복원하거나 Reset을 다시 실행하지 않았습니다.

### Reset 전후 HEAD — 문서 작성 시 사후 조회

다음은 문서 작성 시 실행한 조회 명령과 실제 출력입니다. Reset 직후의 `git log -1` 출력이 아닙니다.

```sh
git reflog show feature/2-round-2-heoney --date=iso --format='%h %gd: %gs' --grep-reflog='reset: moving to HEAD~1'
```

```text
0ed95d3 feature/2-round-2-heoney@{2026-10-21 14:24:57 +0900}: reset: moving to HEAD~1
```

커밋과 부모 조회 명령:

```sh
git show -s --format='commit %H%nparents %P%nsubject %s' 26256ba 0ed95d3 a7b9a5d
```

실제 출력:

```text
commit 26256ba4080270c51d4019dfa19dc95985d2dcff
parents 0ed95d31981fd61625fb7e8ea1940e994c1a57e7
subject docs: add reset practice note
commit 0ed95d31981fd61625fb7e8ea1940e994c1a57e7
parents fbfddd49785fc2df9e8e8edc1c837870e6ce16dc 0f033fb4626bf3025edf2af9bc8ea5b599ecf9f1
subject merge: resolve member 2 round 2 whitespace conflict
commit a7b9a5d210baab3ce1e6e47bfcfeb6a394527efa
parents 0ed95d31981fd61625fb7e8ea1940e994c1a57e7
subject docs: retain reset practice changes
```

인계 기록의 Reset 전 HEAD는 `26256ba`입니다. 현재 조회에서도 이 커밋의 부모가 `0ed95d3`이며,
reflog의 Reset 도착점이 `0ed95d3`임을 확인했습니다. 재커밋 `a7b9a5d`도 같은 부모를 가집니다.

취소한 커밋과 재커밋의 파일 내용 비교:

```sh
git diff --exit-code 26256ba a7b9a5d
```

실제 결과는 출력 없음, 종료 코드 0입니다. 두 커밋의 파일 트리에 차이가 없음을 확인했습니다.

재커밋에 보관된 실습 파일 조회:

```sh
git show a7b9a5d:docs/practice/member-2-reset.md
```

실제 출력:

```text
2번 reset 실습: 커밋 취소 후 변경 유지 확인
```

### 관련 커밋

- Reset 전 실습 커밋: `26256ba4080270c51d4019dfa19dc95985d2dcff` — Push 전 취소한 로컬 커밋으로, 위 조회 결과를 보관했습니다.
- [Reset 후 HEAD / 충돌 해결 커밋 0ed95d3](https://github.com/codyssey-kr/B2-2/commit/0ed95d31981fd61625fb7e8ea1940e994c1a57e7)
- [변경을 유지한 재커밋 a7b9a5d](https://github.com/codyssey-kr/B2-2/commit/a7b9a5d210baab3ce1e6e47bfcfeb6a394527efa)
- [실습 과정 기록 49bfb81](https://github.com/codyssey-kr/B2-2/commit/49bfb81)
- [실습 상태 표 갱신 8e6dca5](https://github.com/codyssey-kr/B2-2/commit/8e6dca5)
- [리뷰 반영 및 실습 파일 삭제 42a7761](https://github.com/codyssey-kr/B2-2/commit/42a7761)
