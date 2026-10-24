name= input("Name:") 
weight = float(input("Weight (kg): "))
height_cm = int(input("Height (cm): "))

height_m=height_cm / 100

bmi=weight / (height_m **2)

water_per_day = weight * 0.033

cleaned_name=name.strip().title()

print("-" * 35)
print(f"Hi {cleaned_name}!")
print(f"BMI        : {bmi:.1f}")          
print(f"Water / day: {water_per_day:.2f} L")  
print("-" * 35)
