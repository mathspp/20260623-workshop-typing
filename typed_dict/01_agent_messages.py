"""
Use a `TypedDict` to encode the structure of the dictionaries that can be added to the list `context`.
"""

from typing import Any


class Message(...):
    ...


context: list[dict[str, Any]] = []

context.append(
    {
        "role": "user",
        "content": "Tell me a joke.",
    }
)

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
