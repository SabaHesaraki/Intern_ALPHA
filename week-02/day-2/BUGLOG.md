# Task 02.2.BUG – Debug Lab

## What this code does:

### Part 1: Nested Loops with `break`
- **What happens:** We have a loop inside another loop. The `break` command only stops the **inner** loop (the current row), not both loops. 
- **Rule to remember:** `break` only escapes the closest loop it belongs to.
- **Output:**
```text

  10
  20 21
  30
  

output = 30
