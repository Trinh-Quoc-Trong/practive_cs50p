import re
import sys


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    text = input("Input: ")
    print(emojize_text(text))


def emojize_text(text: str) -> str:
    try:
        import emoji 
    except ModuleNotFoundError:
        return _emojize_fallback(text)

    text = emoji.emojize(text, language="alias")
    text = emoji.emojize(text, language="en")
    return text


_FALLBACK = {
    ":thumbs_up:": "👍",
    ":thumbsup:": "👍",
    ":smile:": "😄",
    ":grinning:": "😀",
    ":red_heart:": "❤️",
}


def _emojize_fallback(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        token = match.group(0)
        return _FALLBACK.get(token, token)

    return re.sub(r":[a-zA-Z0-9_+\-]+:", repl, text)


if __name__ == "__main__":
    main()
