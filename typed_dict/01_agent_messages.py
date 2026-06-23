"""
Use a `TypedDict` to encode the structure of the dictionaries that can be added to the list `context`.
"""

from typing import Any, TypedDict, NotRequired, Literal


class ContentDict(TypedDict):
    type: Literal["text"]
    text: str


class Message(TypedDict):
    role: str
    content: str | list[ContentDict]
    status: NotRequired[str]


context: list[Message] = []

context.append(
    {
        "role": "assistant",
        "content": [
            {
                "type": "txt",
                "text": "Sure, here's a joke:\n",
            },
            {
                "type": "txt",
                "text": "What's brown and sticky..? A stick!",
            }
        ],
        "status": "completed",  # Could also be 'in_progress'.
    }
)


context.append(
    {
        "role": "user",
        "content": "Tell me a joke.",
    }
)