"""의도적인 오류가 있는 연습용 구현. 담당 feature 브랜치에서 수정하세요.

A 담당: 공백을 정리한 문장을 대문자로 바꾸기."""

from common import normalize_spaces


def to_upper(text: str) -> str:
    """공백을 정리한 문장을 대문자로 반환한다.

    구현 후 예시: to_upper("  Hello   Team  ") == "HELLO TEAM"
    """
    text = normalize_spaces(text)
    return text.capitalize()


if __name__ == "__main__":
    print(to_upper("  Hello   Team  "))  # 구현 후 예상: HELLO TEAM
