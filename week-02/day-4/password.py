def check_password(pw: str) -> str:
    errors = []
    
    # 1. Check length
    if len(pw) < 10:
        errors.append("too short")
        
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*"
    
    # Loop over characters to check conditions
    for char in pw:
        if 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in special_chars:
            has_special = True
            
    if not has_upper:
        errors.append("no uppercase")
    if not has_lower:
        errors.append("no lowercase")
    if not has_digit:
        errors.append("no digit")
    if not has_special:
        errors.append("no special character")
        
    # Check forbidden word 'password' (case-insensitive)
    if "password" in pw.lower():
        errors.append("contains the word password")
        
    if errors:
        return "; ".join(errors)
    return "strong"


# --- Assert Examples 
if __name__ == "__main__":
    assert check_password("Abc!2") == "too short"
    assert check_password("tehran rain") == "no uppercase; no digit; no special character"
    assert check_password("MyPassword!2026") == "contains the word password"
    assert check_password("Tehran#Rain2026") == "strong"
    assert check_password("short!A1") == "too short"
    assert check_password("alllowercase1!_") == "no uppercase"
    assert check_password("ALLUPPERCASE1!_") == "no lowercase"
    assert check_password("NoSpecial123") == "no special character"
    print("All assertions passed successfully!")

