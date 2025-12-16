from pathlib import Path
import string


def read_file(file_path: Path) -> str:
    """
    Reads text from a file and returns it as a string.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def clean_and_tokenize(text: str) -> list[str]:
    """
    Cleans text and splits it into words.
    """
    text = text.lower()

    for symbol in string.punctuation:
        text = text.replace(symbol, " ")

    words = text.split()
    return words
