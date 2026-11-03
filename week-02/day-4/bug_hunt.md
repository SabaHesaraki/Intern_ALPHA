# Bug Hunt Report - Task 02.4.B

## 1. Manual Expected Output
- `final_report(90, 80, 50)` -> `85.0 B`
- `final_report(70, 95, 85, bonus=5)` -> `95.0 A`

## 2. Bugs Found and Fixed

### Bug 1: Incorrect variable assignment in `drop_lowest_average`
- **Symptom:** When `c` is the lowest score, `lowest` incorrectly takes the value of `b`.
- **Breakpoint / Watch:** Checked `lowest` variable in VS Code debugger.
- **Fix:** Changed `lowest = b` to `lowest = c`.

### Bug 2: Incorrect division denominator
- **Symptom:** The sum is divided by 3 (`/ 3`) after dropping one score, instead of 2.
- **Breakpoint / Watch:** Inspected return value in `pdb`.
- **Fix:** Changed division denominator from `3` to `2`.

### Bug 3: Incorrect order of `if-elif` statements in `letter` function
- **Symptom:** `score >= 60` was checked first, returning `"D"` for any passing grade.
- **Breakpoint / Watch:** Debugged step-by-step execution in `pdb`.
- **Fix:** Reordered conditions in descending order (`90`, `80`, `70`, `60`).

### Bug 4: Bonus not assigned to average
- **Symptom:** `avg + bonus` was evaluated but not stored back into `avg`.
- **Breakpoint / Watch:** Watched `avg` variable before calling `letter(avg)`.
- **Fix:** Updated to `avg = avg + bonus`.

