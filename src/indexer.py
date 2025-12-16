from pathlib import Path

from src.processor import read_file, clean_and_tokenize


def build_index(files: list[Path]) -> dict:
    """
    Builds a word-to-files index from a list of files.
    """
    index = {}

    for file_path in files:
        text = read_file(file_path)
        words = clean_and_tokenize(text)

        for word in words:
            if word not in index:
                index[word] = []

            if file_path.name not in index[word]:
                index[word].append(file_path.name)

    return index
