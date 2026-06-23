from typing import TypedDict


class PlayerStatus(TypedDict, total=False):
    name: str
    level: int
    position: tuple[int, int]


player: PlayerStatus = {
    "name": "rgs",
    "level": 3,
}

print(player["position"])