try:
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

