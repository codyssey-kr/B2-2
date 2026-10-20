"""문장을 대문자로 바꾼다."""

from src.common import normalize_spaces


def to_upper(text: str) -> str:
    """문장을 대문자로 바꾼다. 입력의 공백 처리 방식은 작업 브랜치에서 결정한다."""
    text = text  # 공백 처리 구현 위치
    return text.upper()


if __name__ == "__main__":
    print(to_upper("  Hello   Team  "))  # 공백 정리 완료 후 예상: HELLO TEAM
