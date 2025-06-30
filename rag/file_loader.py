from pathlib import Path

def load_file(file_path): 
    if file_path.endswith(".txt"):
        return Path(file_path).read_text(encoding="utf-8")
    raise ValueError("TXT file is required!")