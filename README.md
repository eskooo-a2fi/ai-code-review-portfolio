# AI-Generated Code Review — Fibonacci Case Study

[![Fibonacci tests](https://github.com/eskooo-a2fi/ai-code-review-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/eskooo-a2fi/ai-code-review-portfolio/actions/workflows/ci.yml)

**A structured technical review of deliberately flawed, AI-generated-style Python code.** This case study demonstrates how to identify a subtle correctness issue, explain an inefficient algorithm, rewrite it responsibly and verify the correction with automated tests.

## Review at a glance

| Finding | Why it matters | Recommendation |
| --- | --- | --- |
| **Correctness** | Incorrect base case produces the wrong sequence for boundary inputs | Define and assert the conventional `F(0)=0, F(1)=1` contract |
| **Performance** | Naive recursive calls repeat work, approaching exponential runtime | Use an iterative O(n)-time approach |
| **Maintainability** | Ambiguous variable names obscure state transitions | Use meaningful identifiers and type hints |
| **Input contract** | Undocumented edge cases may mask faulty output | Specify and test supported input types and ranges |

**[Read the full professional code-review report](CODE_REVIEW_REPORT.md)**

## Files

- [`flawed_fibonacci.py`](flawed_fibonacci.py) — intentionally incorrect example for analysis, **not for use in production**.
- [`corrected_fibonacci.py`](corrected_fibonacci.py) — improved implementation.
- [`test_fibonacci.py`](test_fibonacci.py) — reproducible regression tests.
- [`CODE_REVIEW_REPORT.md`](CODE_REVIEW_REPORT.md) — severity, evidence, recommendations and AI-model feedback.

## Run the tests

```bash
python -m pip install pytest
python -m pytest -q
```

This is an educational code-review scenario, not evidence that a particular outside AI service generated these bugs. In an interview, discuss how you isolated a failing boundary case, separated correctness from performance, and defined tests that would catch regressions.

## What I'd improve next

Add property-based tests, runtime benchmarks across increasing `n`, and an automated review rubric covering security, performance and maintainability for a larger multi-file project.

## Evidence and edge cases

**CV keywords demonstrated:** **Python**, **Code Review**, **Debugging**, **Logic Evaluation**, **Flaw Identification**, **Structured Feedback**, **Algorithmic Logic**, **Technical Writing**, **GitHub**, and **AI-Assisted Development** as an evaluation workflow.

In addition to explicit boundaries and invalid input types, `test_properties.py` checks the Fibonacci recurrence across fifty terms. That catches changes which might still pass a few hand-picked examples. The intentionally flawed function remains named `thing(x)` **only because poor naming is one of the review findings**; the corrected implementation uses descriptive names.

The report analyses a fabricated AI-output example. It is not evidence of having evaluated a real client's AI model or of using Claude/ChatGPT in a documented production review.
