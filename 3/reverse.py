"""문장의 단어 순서를 뒤집는다."""

from src.common import normalize_spaces


def reverse_words(text):
    text = normalize_spaces(text)
    return " ".join(text.split()[::-1])


if __name__ == "__main__":
    print(reverse_words("  Hello   Team  "))  # 공백 정리 완료 후 예상: Team Hello
