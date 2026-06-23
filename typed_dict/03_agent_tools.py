"""
DON'T RUN THIS CODE.
The function `edit` is a real piece of code from a coding agent I wrote.
The argument `command` must follow a specific structure based on the key `command["command"]`.
Create a union of TypedDicts that improves the type safety of the function `edit`.
When you're done, the code at the bottom should pass type checking.
"""

from pathlib import Path
import shutil
import time
from typing import Any


def edit(command: dict[str, Any]) -> tuple[bool, str]:
    """Handle Anthropic's Text Edit command."""
    filepath = command["path"]
    path = Path(filepath)

    match command:
        case {"command": "view"}:
            if not path.exists():
                return True, f"{filepath} doesn't exist."
            if path.is_file():
                contents = path.read_text(encoding="utf8").splitlines()
                from_, to_ = command.get("view_range", (0, -1))
                to_ = len(contents) if to_ == -1 else to_
                contents = [
                    line
                    for lineno, line in enumerate(contents, start=1)
                    if from_ <= lineno <= to_
                ]
                return False, "\n".join(contents)

            else:  # Directory
                try:
                    return False, ", ".join(map(str, path.iterdir()))
                except Exception:
                    return True, f"Failed to list directory {path}."

        case {"command": "insert", "insert_line": lineno, "insert_text": text}:
            if not path.exists():
                return True, f"{filepath} doesn't exist."
            if not path.is_file():
                return True, f"{path} isn't a file."

            # Create backup
            backup_path = Path(str(path) + f".{time.strftime('%Y%m%d%H%M%S')}.bkup")
            shutil.copy2(path, backup_path)

            lines = path.read_text(encoding="utf8").splitlines(keepends=True)
            lines.insert(lineno, text)
            print(f"About to write {lines}")
            path.write_text("".join(lines), encoding="utf8")
            return False, f"Successfully inserted requested text in {path}."

        case {"command": "str_replace", "old_str": old, "new_str": new}:
            if not path.exists():
                return True, f"{filepath} doesn't exist."
            if not path.is_file():
                return True, f"{path} isn't a file."

            # Create backup
            backup_path = Path(str(path) + f".{time.strftime('%Y%m%d%H%M%S')}.bkup")
            shutil.copy2(path, backup_path)

            contents = path.read_text(encoding="utf8")
            new_contents = contents.replace(old, new)
            if contents == new_contents:
                return True, "There was no match to replace."
            path.write_text(new_contents, encoding="utf8")
            return False, "Replacement successful."

        case {"command": "create", "file_text": text}:
            if path.exists():
                return True, f"{path} already exists."
            path.write_text(text, encoding="utf8")
            return False, "File created successfully."

        case _:
            raise RuntimeError(f"Can't handle {command = }.")


commands = [
    {
        "command": "view",
        "path": "README.md",
    },
    {
        "command": "view",
        "path": "src/main.py",
        "view_range": (10, 25),
    },
    {
        "command": "insert",
        "path": "src/main.py",
        "insert_line": 12,
        "insert_text": "print('hello')\n",
    },
    {
        "command": "str_replace",
        "path": "src/main.py",
        "old_str": "hello",
        "new_str": "goodbye",
    },
    {
        "command": "create",
        "path": "notes.txt",
        "file_text": "Remember to learn TypedDict.\n",
    },
]


for command in commands:
    error, message = edit(command)
    print(message)
