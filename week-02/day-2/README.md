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

# Task 02.2.C – ASCII Art with Nested Loops

## Description
A Python script that takes an integer `n` (between 2 and 15) from the user with input validation, and prints 4 different ASCII patterns using genuine nested loops (without string multiplication for pattern building).

---

## Pattern Analysis (Pattern 4 - Diamond)

### Question 1: How many times does Pattern 4 call `print()`?
- **Outer loops (per row):** The upper half runs for $i = 1, 3, 5, \dots, n$ (approx. $\frac{n+1}{2}$ rows). The lower half runs for $i = n-2, n-4, \dots, 1$ (approx. $\frac{n-1}{2}$ rows). Total rows = $n$ (if $n$ is odd) or similar.
- **Inside each row:** 
  1. Print spaces (loop).
  2. Print stars (loop).
  3. Print a newline `print()` at the end of the row.
- Therefore, `print()` inside the loops is called **once per row** to move to the next line, meaning it is called **$n$ times** (once for each printed row).

### Question 2: How many total times does the inner loop execute for Pattern 4?
- The inner loops handle spaces and stars for each row. Across all rows of the diamond, the total iterations of the inner loops roughly scale with **$O(n^2)$** (proportional to the area of the bounding box of the diamond).

---

## Sample Outputs

### For `n = 4`:
```text
pattern 1 (right triangle)
*
**
***
****

pattern 2 (number triangle)
1
12
123
1234

pattern 3 (hollow square)
****
*  *
*  *
****

pattern 4 (diamond)
 *
***
 *

