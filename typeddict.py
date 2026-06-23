from typing import TypedDict


class PlayerStatus(TypedDict):
    name: str
    level: int
    position: tuple[int, int]


player: PlayerStatus = {
    "name": "rgs",
    "level": 3,
    "position": (3, 0),
}

print(player["nick"])