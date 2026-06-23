"""
Part of the implementation of a game.
"""

from enum import StrEnum, auto
from typing import Any, Literal, overload


class Action(StrEnum):
    MOVE = auto()
    TALK = auto()
    SLEEP = auto()
    LEVEL_UP = auto()


@overload
def process_action(
    player_status: dict[str, Any],
    action: Literal[Action.MOVE],
    dx: int, dy: int,
) -> dict[str, Any]: ...

@overload
def process_action(
    player_status: dict[str, Any],
    action: Literal[Action.TALK],
    message: str,
) -> dict[str, Any]: ...

@overload
def process_action(
    player_status: dict[str, Any],
    action: Literal[Action.SLEEP],
) -> dict[str, Any]: ...

@overload
def process_action(
    player_status: dict[str, Any],
    action: Literal[Action.LEVEL_UP],
) -> dict[str, Any]: ...


def process_action(
    player_status: dict[str, Any],
    action: Action,
    *args: int | str,
) -> dict[str, Any]:
    match action:
        case Action.MOVE:
            dx, dy = args
            x, y = player_status["position"]
            return {
                **player_status,
                "position": (x + dx, y + dy),
            }

        case Action.TALK:
            message = args[0]
            print(f'{player_status["nick"]} says: {message}')
            return player_status

        case Action.SLEEP:
            return {
                **player_status,
                "status_condition": "sleeping",
            }

        case Action.LEVEL_UP:
            return {
                **player_status,
                "level": player_status["level"] + 1,
            }

player = {
    "name": "rgs",
    "level": 3,
    "position": (3, 0),
}
process_action(player, Action.MOVE, 1, 1)
process_action(player, Action.TALK, "Hello!")
process_action(player, Action.SLEEP)
process_action(player, Action.LEVEL_UP)
