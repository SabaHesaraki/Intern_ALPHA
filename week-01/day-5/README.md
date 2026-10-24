# Day 05 - Python Basics

## Task 01.5.A: BMI & Water Calculator
- File: `health.py`
- Description: Calculates user BMI and daily water needed based on weight and height.

## Task 01.5.B: Time Analyzer
- File: `seconds.py`
- Description: Changes total seconds into days, hours, minutes, and seconds using `divmod`.

### Trace Table for Input `200000` seconds:

| Step | Variable | Value | Description |
| :--- | :--- | :--- | :--- |
| Input | `total_seconds` | `200000` | User enters seconds |
| Divide by 86400 | `days` / `rest` | `2` / `27200` | Get days and rest |
| Divide by 3600 | `hours` / `rest` | `7` / `2000` | Get hours and rest |
| Divide by 60 | `minutes` / `seconds` | `33` / `20` | Get minutes and seconds |
| Result | - | `2 days, 07:33:20` | Final formatted time |

## Task 01.5.C: Text Lab
- File: `text_lab.py`
- Description: Analyzes a given sentence (counts characters, words, makes upper/reversed text, counts letters, creates a slug, finds first/last words, and checks for python).

### Testing with a Persian Sentence ("سلام دنیا خوش آمدید"):
- **chars (with spaces):** 20
- **chars (no spaces):** 17
- **words:** 3
- **upper:** سلام دنیا خوش آمدید (Persian letters do not change)
- **reversed:** دیدمآ خوش انید دنیا ملاس (Characters reversed)
- **first / last word:** سلام / آمدید
- **Crash Test:** Passed successfully with no errors!

## Task 01.5.PRED: Simple Explanations

- **Snippet 1:** Shows how `*` repeats a string and multiplies numbers. It also shows how `int()` changes a string to a number and how `//` works with negative numbers.
- **Snippet 2:** Shows that strings do not change when we use a method like `strip()`, unless we save the result. It also uses `strip().upper()` and `[::-1]` to clean, capitalize, and reverse a string.
- **Snippet 3:** Shows the order of math operations, small differences in decimal calculations, and how `round()` and `int()` work. Python's `round()` can round `.5` to the nearest even number. `int()` removes the decimal part.

---

## Daily Reflection

- **What I built:** I made programs to calculate health information, change seconds into time, analyze text, and test Python code.
- **What was hard:** I learned that decimal numbers can have small calculation differences. I also learned how Python rounds numbers like `2.5` and `3.5`.
- **How to run:** Open the terminal and run a program with `uv run python <script_name>.py`.
- **AI usage:** I used AI to understand the tasks, check my code, and write simple explanations.

