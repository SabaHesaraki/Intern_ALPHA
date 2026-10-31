# Task 02.2.B – Grade Stats with Sentinel

## Description
A Python script that collects integer scores (between 0 and 100) from the user until `done` or `DONE` is entered. It computes total count, sum, average, maximum, minimum, and pass rate (scores >= 50) without using lists or built-in `min()` / `max()`.

## Trace Table (Inputs: 78, 45, 92, done)

| Step | User Input | Action / Condition | count | total_sum | max_score | min_score | passed_count |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Initial | - | Initialize variables | 0 | 0 | None | None | 0 |
| Loop 1 | `78` | Valid score (>= 50: True) | 1 | 78 | 78 | 78 | 1 |
| Loop 2 | `45` | Valid score (>= 50: False) | 2 | 123 | 78 | 45 | 1 |
| Loop 3 | `92` | Valid score (>= 50: True) | 3 | 215 | 92 | 45 | 2 |
| Loop 4 | `done` | Sentinel matched -> Break | 3 | 215 | 92 | 45 | 2 |

### Final Calculated Metrics:
- **count:** 3
- **sum:** 215
- **avg:** 215 / 3 = 71.7
- **max:** 92
- **min:** 45
- **passed:** 2 (66.7%)

