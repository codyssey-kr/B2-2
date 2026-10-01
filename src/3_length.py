"""의도적인 오류가 있는 연습용 구현. 담당 feature 브랜치에서 수정하세요.

C 담당: 공백을 정리한 문장의 글자 수 세기."""

from common import normalize_spaces


def count_characters(text: str) -> int:
    """공백을 정리한 문장의 글자 수를 센다. 중간 공백도 포함한다.

    구현 후 예시: count_characters("  Hello   Team  ") == 10
    """
    text = normalize_spaces(text)
    return len(text.replace(" ", ""))


if __name__ == "__main__":
    print(count_characters("  Hello   Team  "))  # 구현 후 예상: 10
