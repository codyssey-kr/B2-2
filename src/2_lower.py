"""의도적인 오류가 있는 연습용 구현. 담당 feature 브랜치에서 수정하세요.

B 담당: 공백을 정리한 문장을 소문자로 바꾸기."""

from common import normalize_spaces


def to_lower(text: str) -> str:
    """공백을 정리한 문장을 소문자로 반환한다.

    구현 후 예시: to_lower("  Hello   Team  ") == "hello team"
    """
    text = normalize_spaces(text)
    return text.upper()


if __name__ == "__main__":
    print(to_lower("  Hello   Team  "))  # 구현 후 예상: hello team
