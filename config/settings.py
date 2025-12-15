from pathlib import Path

# Folder containing notes to search
NOTES_DIR = Path("notes")

# Where the search index will live later (not used yet today)
INDEX_PATH = Path("data/index.json")

# File types we consider "notes"
SUPPORTED_EXTENSIONS = {".txt", ".md"}
