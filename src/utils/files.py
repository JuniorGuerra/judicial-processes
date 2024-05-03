import json
from typing import List, Any

def load_file(file_path: str) -> List[dict]:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError) as error:
        print(error)
        return []
    