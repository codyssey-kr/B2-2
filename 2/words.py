"""공백으로 구분한 단어 수를 센다."""

from src.common import normalize_spaces


def count_words(text: str) -> int:
    """공백으로 구분한 단어 수를 센다. 입력의 공백 처리 방식은 작업 브랜치에서 결정한다."""
    text = text  # 공백 처리 구현 위치
    return len(text.split())


if __name__ == "__main__":
    print(count_words("  Hello   Team  "))  # 공백 정리 완료 후 예상: 2
