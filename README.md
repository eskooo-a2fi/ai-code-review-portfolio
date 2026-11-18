# AI Code Review Portfolio · Fibonacci case study

A professional review of deliberately flawed, AI-generated-style Python. The report identifies a subtle base-case defect, exponential time complexity, weak naming, and missing validation; then proposes and tests an O(n) iterative replacement.

## Contents
- `flawed_fibonacci.py` — deliberately unsafe/inaccurate educational example; do not ship it.
- `corrected_fibonacci.py` — corrected, documented implementation.
- `test_fibonacci.py` — pytest validation and edge cases.
- `CODE_REVIEW_REPORT.md` — findings, severity, evidence, acceptance criteria, and feedback for an AI model.

## Run

```bash
python -m pip install pytest
python -m pytest -q
python flawed_fibonacci.py    # intentionally prints incorrect values
```

## GitHub

```bash
git init
git add .
git commit -m "Document AI-generated Python code review"
gh repo create ai-code-review-portfolio --public --source=. --remote=origin --push
```

The tests verify the *corrected* implementation. If discussing this in an interview, explain how you detected the defect using `F(0)`, quantified the time complexity, and built regression tests.
