# AI-Generated Code Evaluation · Structured Review Report

**Case ID:** AI-FIB-001  
**Language:** Python 3.11+  
**Scope:** Functional accuracy, computational efficiency, readability, and input validation  
**Verdict:** **Changes required** — the submitted function is not correct or robust enough for reuse.

## 1. Original AI output (intentionally flawed)

```python
def thing(x):
    """Return the x-th Fibonacci number (F(0)=0, F(1)=1)."""
    if x <= 1:
        return 1
    return thing(x - 1) + thing(x - 2)
```

## 2. Review findings

| ID | Severity | Finding | Evidence and impact | Recommendation |
| --- | --- | --- | --- | --- |
| FIB-01 | **High** | Incorrect base case / logic | `thing(0)` returns `1`, contradicting the documented `F(0)=0`. All values derived from that wrong base case are shifted: `thing(2)=2` but `F(2)=1`. | Return `n` when `n <= 1`, after input validation. |
| FIB-02 | **High** | Exponential time complexity | Naive recursion repeats the same subproblems. Runtime grows as roughly `O(φ^n)` and will be impractical for moderately large `n` (the function also risks recursion-depth failure). | Use bottom-up iteration: `O(n)` time, `O(1)` additional memory. |
| FIB-03 | **Medium** | Ambiguous names | `thing` and `x` conceal the function's purpose and parameter meaning. This raises maintenance and review costs. | Rename them `fibonacci` and `n`; document the sequence convention. |
| FIB-04 | **Medium** | No input contract | Negative integers, booleans and non-integer inputs have no appropriate validation. For example, `thing(-4)` incorrectly returns 1 and `thing(True)` returns 1 because `bool` is an `int` subclass. | Reject negatives and non-integer types explicitly. |

## 3. Corrected implementation

```python
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
```

The implementation maintains the invariant that before each loop iteration, `previous=F(k)` and `current=F(k+1)`. Each update shifts the pair forward. After `n` iterations, `previous=F(n)`.

## 4. Test strategy and outcome

| Scenario | Input | Expected |
| --- | --- | --- |
| First term | `0` | `0` |
| Second term | `1` | `1` |
| Standard case | `10` | `55` |
| Larger input | `100` | `354224848179261915075` |
| Negative | `-1` | `ValueError` |
| Incorrect type | `True`, `3.5`, `'5'`, `None` | `TypeError` |

Execute `python -m pytest -q`. The repository includes automated checks in `test_fibonacci.py` and two full Python source files. **Do not label tests 'passed' until you run them.**

## 5. Feedback to the generating AI

> Your implementation did not match its declared Fibonacci definition because the zero-index base case was wrong. It also re-computed overlapping subproblems, giving exponential runtime and poor scalability. Rename the function and parameter to reveal intent, validate the input contract, and replace naive recursion with an iterative algorithm. Verify the boundary cases `n=0`, `n=1` and `n=2`, then test both invalid inputs and a large valid input. Report the exact tests executed, not just a claim of correctness.

**Overall quality assessment:** This review separates functional correctness, runtime complexity, maintainability and robustness, and specifies directly verifiable acceptance criteria. For extremely large indices, consider an O(log n) fast-doubling algorithm if performance requirements justify the extra complexity.
