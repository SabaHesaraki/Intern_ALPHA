def drop_lowest_average(a: int, b: int, c: int) -> float:
    lowest = a
    if b < lowest:
        lowest = b
    if c < lowest:
        lowest = c
    # Bug fixed: divided by 2 instead of 3
    return (a + b + c - lowest) / 2

def letter(score: float) -> str:
    # Bug fixed: proper descending order for score grades
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def final_report(a: int, b: int, c: int, bonus: int = 0) -> str:
    avg = drop_lowest_average(a, b, c)
    # Bug fixed: assigned bonus back to avg
    avg = avg + bonus
    if avg > 100:
        avg = 100
    return f"{avg:.1f} {letter(avg)}"

# Assertions for validation
assert final_report(90, 80, 50) == "85.0 B"
assert final_report(70, 95, 85, bonus=5) == "95.0 A"
print("All assertions passed successfully!")

