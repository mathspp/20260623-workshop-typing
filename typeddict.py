from typing import TypedDict, Required

"""
class PlayerStatus(TypedDict):
    name: str
    level: int
    position: tuple[int, int]
    status_condition: NotRequired[str]
"""

class PlayerStatus(TypedDict, total=False):
    name: str
    level: int
    position: tuple[int, int]
    status_condition: NotRequired[str]


player: PlayerStatus = {
    "name": "rgs",
    "level": 3,
    "position": (3, 0),
}

print(player["position"])