"""문장의 단어 순서를 뒤집는다."""

from src.common import normalize_spaces


def reverse_words(text: str) -> str:
    """문장의 단어 순서를 뒤집는다. 입력의 공백 처리 방식은 작업 브랜치에서 결정한다."""
    text = text  # 공백 처리 구현 위치
    return " ".join(reversed(text.split()))


if __name__ == "__main__":
    print(reverse_words("  Hello   Team  "))  # 공백 정리 완료 후 예상: Team Hello
