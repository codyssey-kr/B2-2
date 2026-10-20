"""빈 문장이 아니면 끝에 느낌표를 붙인다."""

from src.common import normalize_spaces


def add_exclamation(text: str) -> str:
    """빈 문장이 아니면 끝에 느낌표를 붙인다. 입력의 공백 처리 방식은 작업 브랜치에서 결정한다."""
    text = text  # 공백 처리 구현 위치
    return text + "!" if text else ""


if __name__ == "__main__":
    print(add_exclamation("  Hello   Team  "))  # 공백 정리 완료 후 예상: Hello Team!
