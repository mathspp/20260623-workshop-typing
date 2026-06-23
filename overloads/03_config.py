"""
The function `get_config` is SURE to return a string if you provide a string as the default.
Use an @overload to encode that information so that the calls to `reveal_type` agree with the comments.
"""

from typing import reveal_type


config = {
    "host": "localhost",
    "mode": "development",
    "log_level": "info",
}


def get_config(key: str, default: str | None = None) -> str | None:
    return config.get(key, default)


host = get_config("host")
reveal_type(host)  # Should be `str | None`

username = get_config("username")
reveal_type(username)  # Should be `str | None`

fallback_username = get_config("username", "guest")
reveal_type(fallback_username)  # Should be `str`

log_level = get_config("log_level", "warning")
reveal_type(log_level)  # Should be `str`
