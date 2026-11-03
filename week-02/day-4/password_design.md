# Password Validator Design - Task 02.4.A

## 1. Understand
The goal is to create a robust password validator function in Python that checks if a given password meets specific security criteria. It must return a string listing all unmet criteria separated by a semicolon and space (`; `), or return the exact word `"strong"` if all rules are satisfied.

### Requirements:
- Minimum length of 10 characters.
- Must contain at least one uppercase letter (A-Z).
- Must contain at least one lowercase letter (a-z).
- Must contain at least one digit (0-9).
- Must contain at least one special character from `!@#$%^&*`.
- Must NOT contain the forbidden word "password" (case-insensitive).

---

## 2. Decomposition
```mermaid
graph TD
A[Start: check_password pw] --> B{Length >= 10?}
B -- No --> C[Add length error]
B -- Yes --> D{Has Uppercase?}
D -- No --> E[Add uppercase error]
D -- Yes --> F{Has Lowercase?}
F -- No --> G[Add lowercase error]
F -- Yes --> H{Has Digit?}
H -- No --> I[Add digit error]
H -- Yes --> J{Has Special Char?}
J -- No --> K[Add special char error]
J -- Yes --> L{Contains 'password'?}
L -- Yes --> M[Add forbidden word error]
L -- No --> N{Any errors collected?}
C --> D
E --> F
G --> H
I --> J
K --> L
M --> N
N -- Yes --> O[Return errors joined by '; ']
N -- No --> P[Return 'strong']
## 3.Pseudocode
FUNCTION check_password(pw):
errors = []

// Check length
IF length of pw < 10 THEN
APPEND "password must be at least 10 characters long" to errors
END IF

// Check character types using a loop
has_upper = FALSE
has_lower = FALSE
has_digit = FALSE
has_special = FALSE
special_chars = "!@#$%^&*"

FOR EACH char IN pw:
IF char is uppercase THEN set has_upper = TRUE
IF char is lowercase THEN set has_lower = TRUE
IF char is digit THEN set has_digit = TRUE
IF char IN special_chars THEN set has_special = TRUE
END FOR

IF has_upper == FALSE THEN APPEND "password must contain at least one uppercase letter" to errors
IF has_lower == FALSE THEN APPEND "password must contain at least one lowercase letter" to errors
IF has_digit == FALSE THEN APPEND "password must contain at least one digit" to errors
IF has_special == FALSE THEN APPEND "password must contain at least one special character (!@#$%^&*)" to errors

// Check forbidden word (case-insensitive)
IF "password" IN lowercase(pw) THEN
APPEND "password cannot contain the word 'password'" to errors
END IF

// Return result
IF length of errors > 0 THEN
RETURN join errors with "; "
ELSE
RETURN "strong"
END IF
END FUNCTION
