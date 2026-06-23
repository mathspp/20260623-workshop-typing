"""
Use a `TypedDict` to encode the structure of the dictionaries that can be added to the list `context`.
"""

from typing import Any, TypedDict, NotRequired


class Message(TypedDict):
    role: str
    content: str | list[dict[str, str]]
    status: NotRequired[str]


context: list[Message] = []

context.append(
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "Sure, here's a joke:\n",
            },
            {
                "tye": "text",
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