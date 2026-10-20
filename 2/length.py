"""중간 공백을 포함한 글자 수를 센다."""

from src.common import normalize_spaces


def count_characters(text: str) -> int:
    """중간 공백을 포함한 글자 수를 센다. 입력의 공백 처리 방식은 작업 브랜치에서 결정한다."""
    text = text.strip()
    return len(text)


if __name__ == "__main__":
    print(count_characters("  Hello   Team  "))  # 공백 정리 완료 후 예상: 10
