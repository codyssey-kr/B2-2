"""팀원별 문자열 함수에서 함께 사용하는 공백 정리 유틸."""


def normalize_spaces(text: str) -> str:
    """앞뒤 공백을 제거하고 연속된 공백 문자를 한 칸으로 합친다.

    >>> normalize_spaces("  Hello\tteam!  ")
    'Hello team!'
    """
    return " ".join(text.split())


def return_text(text: str) -> str:
    """공백을 정리한 문자열을 반환한다."""
    return normalize_spaces(text)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="문장의 연속 공백을 정리합니다.")
    parser.add_argument("text", help="따옴표로 감싼 문장")
    args = parser.parse_args()
    print(normalize_spaces(args.text))
