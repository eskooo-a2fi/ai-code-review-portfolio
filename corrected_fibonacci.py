"""Validated O(n) time, O(1) space Fibonacci implementation."""


def fibonacci(n: int) -> int:
    """Return F(n) for n >= 0, with F(0)=0 and F(1)=1."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError('n must be an integer, not a bool or other type')
    if n < 0:
        raise ValueError('n must be non-negative')
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous
