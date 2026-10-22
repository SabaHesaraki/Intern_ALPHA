# REPL Detective Log

1. 10 / 3
- My guess: 3.33
- Actual output: 3.3333333333333335
- Why: Normal division in Python always returns a float number.

2. 10 // 3
- My guess: 3
- Actual output: 3
- Why: Floor division removes the decimal part.

3. 10 % 3
- My guess: 1
- Actual output: 1
- Why: Gives the remainder of division.

4. 2 ** 10
- My guess: 1024
- Actual output: 1024
- Why: Power operator (2 to the power of 10).

5. "5" + "5"
- My guess: 55
- Actual output: '55'
- Why: Plus sign joins text strings together.

6. "5" * 3
- My guess: 555
- Actual output: '555'
- Why: Multiplying a string repeats it.

7. len("INTERN.EXE")
- My guess: 10
- Actual output: 10
- Why: Counts all characters including the dot.

8. type(3.0)
- My guess: float
- Actual output: <class 'float'>
- Why: Numbers with a dot are floats.

9. type("3")
- My guess: str
- Actual output: <class 'str'>
- Why: Text inside quotes is a string.

10. round(2.675, 2)
- My guess: 2.68
- Actual output: 2.67
- Why: Float binary issue; 2.675 cannot be stored precisely in binary memory, so it rounds down to 2.67.

11. 0.1 + 0.2
- My guess: 0.3
- Actual output: 0.30000000000000004
- Why: Floating-point precision limitation in computers when handling decimals.

12. "Hello".upper()
- My guess: HELLO
- Actual output: 'HELLO'
- Why: Changes all letters to uppercase.

---

### Extra Experiments:

13. True + True
- My guess: 2
- Actual output: 2
- Why: Booleans work as 1 and 0 in calculations.

14. "a" * 0
- My guess: empty
- Actual output: ''
- Why: Multiplying text by zero returns an empty string.

15. bool("")
- My guess: False
- Actual output: False
- Why: Empty strings are evaluated as falsy in Python.

