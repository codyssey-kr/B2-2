"""문장의 첫 단어를 반환한다."""

from src.common import normalize_spaces


def first_word(text: str) -> str:
    """문장의 첫 단어를 반환한다. 빈 입력은 빈 문자열을 반환한다."""
    text = text.strip()
    return text.split(" ")[0]


if __name__ == "__main__":
    print(first_word("  Hello   Team  "))  # 공백 정리 완료 후 예상: Hello
