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
        "role": "assistant",
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
        "role": "user",
        "content": "Tell me a joke.",
    }
)