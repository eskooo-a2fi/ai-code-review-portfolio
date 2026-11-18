"""Purposely wrong AI-generated code for REVIEW ONLY. Do not reuse as a library."""


def thing(x):
    """Return the x-th Fibonacci number (F(0)=0, F(1)=1)."""
    if x <= 1:
        return 1  # BUG: returns 1 for F(0), which should be 0.
    return thing(x - 1) + thing(x - 2)


if __name__ == '__main__':
    for i in range(8):
        print(i, thing(i))
