## 3. Pseudocode
```text
FUNCTION check_password(pw):
errors = []

IF length of pw < 10 THEN
APPEND "password must be at least 10 characters long" to errors
END IF

has_upper = FALSE
has_lower = FALSE
has_digit = FALSE
has_special = FALSE

FOR EACH char IN pw:
IF char is uppercase THEN set has_upper = TRUE
IF char is lowercase THEN set has_lower = TRUE
IF char is digit THEN set has_digit = TRUE
IF char IN "!@#$%^&*" THEN set has_special = TRUE
END FOR

IF has_upper == FALSE THEN APPEND "password must contain at least one uppercase letter" to errors
IF has_lower == FALSE THEN APPEND "password must contain at least one lowercase letter" to errors
IF has_digit == FALSE THEN APPEND "password must contain at least one digit" to errors
IF has_special == FALSE THEN APPEND "password must contain at least one special character" to errors

IF "password" IN lowercase(pw) THEN
APPEND "password cannot contain the word password" to errors
END IF

IF length of errors > 0 THEN
RETURN join errors with "; "
ELSE
RETURN "strong"
END IF
END FUNCTION
