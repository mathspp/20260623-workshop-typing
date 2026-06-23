"""
Use a `TypedDict` to encode the structure of the dictionaries that can be added to the list `context`.
"""

from typing import Any, TypedDict, NotRequired
from enum import StrEnum


class Role(StrEnum):
    USER = "user"
    ASSISTANT = "assistant"


class Content(TypedDict):
    type: str
    text: str


class Message(TypedDict):
    role: Role
    content: str | list[Content]
    status: NotRequired[str]


context: list[Message] = []

context.append(
    {
        "role": Role.ASSISTANT,
        "content": [
            {
                "type": "text",
                "text": "Sure, here's a joke:\n",
            },
            {
                "type": "text",
                "text": "What's brown and sticky..? A stick!",
            }
        ],
        "status": "completed",  # Could also be 'in_progress'.
    }
)


context.append(
    {
        "role": Role.USER,
        "content": "Tell me a joke.",
    }
)