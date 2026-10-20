"""의도적인 오류가 있는 연습용 구현. 담당 feature 브랜치에서 수정하세요.

D 담당: 공백을 정리한 문장의 단어 수 세기."""

from common import normalize_spaces


def count_words(text: str) -> int:
    """공백으로 구분한 단어 수를 반환한다. 빈 문자열은 0이다.

    구현 후 예시: count_words("  Hello   team!  ") == 2
    """
    text = normalize_spaces(text)
    return len(text.split(" "))


if __name__ == "__main__":
    print(count_words("  Hello   Team  "))  # 구현 후 예상: 2
