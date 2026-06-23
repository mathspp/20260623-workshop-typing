def f(
    positional_only,
    /,
    positional_or_kwd,
    *,
    kwd_only,
):
    pass


f(1, 2, kwd_only=5)
f(1, positional_or_kwd=2, kwd_only=5)