try:
    bill = float(input("bill: "))
    tip_percent = int(input("tip percent: "))
    people = int(input("people: "))

    if bill < 0:
        print("bill cannot be negative")
    elif not 0 <= tip_percent <= 100:
        print("tip percent must be between 0 and 100")
    elif people <= 0:
        print("people must be at least 1")
    else:
        tip = bill * tip_percent / 100
        total = bill + tip
        share = total / people
        label = "person" if people == 1 else "people"
        print(f"tip    : {tip:>14,.2f}")
        print(f"total  : {total:>14,.2f}")
        print(f"each of {people} {label}: {share:,.2f}")

    weight = float(input("Weight (kg): "))
    height = float(input("Height (cm): "))

    if weight <= 0:
        print("weight cannot be zero or negative")
    elif height <= 0 or height > 260:
        print("height must be between 1 and 260 cm")
    else:
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"BMI: {bmi:.1f} -> {category}")

except ValueError:
    print("invalid input, please enter numbers only")

