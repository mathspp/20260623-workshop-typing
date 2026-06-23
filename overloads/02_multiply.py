"""
The function `multiply` cannot accept both arguments as strings, otherwise you get an error.
Thus, in the 4 calls to `multiply` at the bottom, one of them should be flagged as wrong.
Use overloads to encode the relationships between `left`, `right`, and the return result.

Even with the overloads, the body of `multiply` shows an error. Can you get rid of the error?
Don't spend more than 5 minutes on that.
"""

from typing import overload, reveal_type

@overload
def multiply(left: int, right: int) -> int: ...
@overload
def multiply(left: int, right: str) -> str: ...
@overload
def multiply(left: str, right: int) -> str: ...

def multiply(left: int | str, right: int | str) -> int | str:
    # Type narrowing — “open problem”: maybe `TypeIs`?
    # (TypeGuard)
    if isinstance(left, int) and isinstance(right, int):
        return left * right
    if isinstance(left, str) and isinstance(right, int):
        return left * right
    if isinstance(left, int) and isinstance(right, str):
        return left * right
    raise TypeError


reveal_type(multiply(3, 4))  # Should be `int`
reveal_type(multiply(3, "4"))  # Should be `str`
reveal_type(multiply("3", 4))  # Should be `str`
reveal_type(multiply("3", "4"))  # Should be disallowed


def my_function() -> list[str] | None:
    raise NotImplementedError

variable = my_function()
assert variable is not None
print(len(variable))