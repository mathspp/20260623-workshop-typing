from typing import overload, reveal_type

@overload
def add(left: int, right: int) -> int: ...

@overload
def add(left: str, right: str) -> str: ...

def add(left: int | str, right: int | str) -> int | str:
    return left + right


reveal_type(add(2, 3))  # int
reveal_type(add("oi", "bye"))  # str
