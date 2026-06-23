"""
Part of the implementation of a game.
"""

from enum import StrEnum, auto
from typing import Any, Literal


class Action(StrEnum):
    MOVE = auto()
    TALK = auto()
    SLEEP = auto()
    LEVEL_UP = auto()


def process_action(
    player_status: dict[str, Any],
    action: Literal["move", "talk", "sleep"],
    *args: int | str,
) -> dict[str, Any]:
    match action:
        case "move":
            dx, dy = args
            x, y = player_status["position"]
            return {
                **player_status,
                "position": (x + dx, y + dy),
            }

        case "talk":
            message = args[0]
            print(f'{player_status["nick"]} says: {message}')
            return player_status

        case "sleep":
            return {
                **player_status,
                "status_condition": "sleeping",
            }

player = {
    "name": "rgs",
    "level": 3,
    "position": (3, 0),
}
process_action(player, Action.MOVE, 1, 1)
process_action(player, "talk", "Hello!")
process_action(player, "sleep")
process_action(player, "level_up")
