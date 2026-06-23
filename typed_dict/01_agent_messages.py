"""
Use a `TypedDict` to encode the structure of the dictionaries that can be added to the list `context`.
"""

from typing import Any, TypedDict


class Message(TypedDict):
    role: str
    content: str


context: list[Message] = []

context.append(
    {
        "role": "user",
        "content": "Tell me a joke.",
    }
)
