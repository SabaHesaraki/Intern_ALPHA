# Password Validator Design

## 1. Understand

### Goal
To build a Python function named `check_password(pw)` that evaluates the strength of a given password string against specific security rules and returns either `"strong"` or a semicolon-separated list of violated rules.

### Input & Output
- **Input:** `pw` (`str`) — The password string to check.
- **Output:** `str` — Returns `"strong"` if all conditions pass. Otherwise, returns error messages combined and separated by `; `.

### Rules & Constraints
1. **Length:** Must be at least 10 characters long.
2. **Uppercase:** Must contain at least one uppercase letter (`A-Z`).
3. **Lowercase:** Must contain at least one lowercase letter (`a-z`).
4. **Digit:** Must contain at least one number (`0-9`).
5. **Special Character:** Must contain at least one special character from: `!@#$%^&*` (no spaces inside).
6. **Forbidden Word:** Must not contain the word `"password"` (case-insensitive).

### Test Cases (8 Examples)
1. `check_password("Abc!2")` -> `"too short"`
2. `check_password("tehran rain")` -> `"no uppercase; no digit; no special character"`
3. `check_password("MyPassword!2026")` -> `"contains the word password"`
4. `check_password("Tehran#Rain2026")` -> `"strong"`
5. `check_password("short!A1")` -> `"too short"`
6. `check_password("alllowercase1!_")` -> `"no uppercase"`
7. `check_password("ALLUPPERCASE1!_")` -> `"no lowercase"`
8. `check_password("NoSpecial123")` -> `"no special character"`

---

## 2. Decomposition
```mermaid
graph TD
A[Start: check_password pw] --> B{Length >= 10?}
B -- No --> C[Add 'too short']
B -- Yes --> D{Loop chars: Check Upper, Lower, Digit, Special}
D --> E{Any missing rule?}
E -- Yes --> F[Append respective error messages]
E -- No --> G{Contains 'password' case-insensitive?}
F --> G
G -- Yes --> H[Add 'contains the word password']
G -- No --> I{Are there any errors?}
H --> I
I -- Yes --> J[Join errors with '; ' and return]
I -- No --> K[Return 'strong']

## 3.Pseudocode 

FUNCTION check_password(pw):
SET errors = []

IF length(pw) < 10:
APPEND "too short" to errors

SET has_upper = FALSE
SET has_lower = FALSE
SET has_digit = FALSE
SET has_special = FALSE
SET special_chars = "!@#$%^&*"

FOR each char IN pw:
IF char is uppercase:
has_upper = TRUE
ELSE IF char is lowercase:
has_lower = TRUE
ELSE IF char is digit:
has_digit = TRUE
ELSE IF char IS IN special_chars:
has_special = TRUE

IF NOT has_upper:
APPEND "no uppercase" to errors
IF NOT has_lower:
APPEND "no lowercase" to errors
IF NOT has_digit:
APPEND "no digit" to errors
IF NOT has_special:
APPEND "no special character" to errors

IF "password" IN lowercase(pw):
APPEND "contains the word password" to errors

IF length(errors) > 0:
RETURN join(errors, "; ")
ELSE:
RETURN "strong"
END FUNCTION

