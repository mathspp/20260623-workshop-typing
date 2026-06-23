from typing import TypedDict, NotRequired, ReadOnly

"""
class PlayerStatus(TypedDict, total=False):
    name: Required[str]
    level: Required[int]
    position: Required[tuple[int, int]]
    status_condition: str
"""


class PlayerStatus(TypedDict):
    # name: ReadOnly[str]  # 3.13+
    name: str
    level: int
    position: tuple[int, int]
    status_condition: NotRequired[str]


player: PlayerStatus = {
    "name": "rgs",
    "level": 3,
    "position": (3, 0),
}
player["name"] = "rodrigo"
print(player)

print(player["position"])