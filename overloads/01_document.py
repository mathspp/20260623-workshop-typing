"""
Run this script. What do you see in the calls to `print` and in the calls to `reveal_type`?
What's the relationship between what's inside the square brackets of `doc` and the result you get?
Use `@overload` to encode that information so that the calls to `reveal_type` reveal the indicated
types when you run the type checker.
"""

from pathlib import Path
from typing import Any, reveal_type

class Document:
    def __init__(self, path: Path) -> None:
        self.path = path

    def __getitem__(self, line_index: int | slice) -> str | list[str]:
        text = self.path.read_text().splitlines()
        return text[line_index]


doc = Document(Path(__file__))
print("\n".join(doc[7]))
# reveal_type(doc[7])  # Should be `str`

print("-" * 30)

print("\n".join(doc[10:17]))
# reveal_type(doc[10:17])  # Should be `list[str]`
