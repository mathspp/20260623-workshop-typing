"""
The function `multiply` cannot accept both arguments as strings, otherwise you get an error.
Thus, in the 4 calls to `multiply` at the bottom, one of them should be flagged as wrong.
Use overloads to encode the relationships between `left`, `right`, and the return result.

Even with the overloads, the body of `multiply` shows an error. Can you get rid of the error?
Don't spend more than 5 minutes on that.
"""

from typing import reveal_type


def multiply(left: int | str, right: int | str) -> int | str:
    return left * right


reveal_type(multiply(3, 4))  # Should be `int`
reveal_type(multiply(3, "4"))  # Should be `str`
reveal_type(multiply("3", 4))  # Should be `str`
reveal_type(multiply("3", "4"))  # Should be disallowed
