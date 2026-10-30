year = int(input("Year: "))
month = int(input("Month (1-12): "))

if not 1 <= month <= 12:
    print("error: month must be between 1 and 12")
else:
    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            days = 31
        case 4 | 6 | 9 | 11:
            days = 30
        case 2:
            days = 29 if leap else 28

    match month:
        case 12 | 1 | 2:
            season = "winter"
        case 3 | 4 | 5:
            season = "spring"
        case 6 | 7 | 8:
            season = "summer"
        case 9 | 10 | 11:
            season = "autumn"

    print(f"year: {year}  month: {month}  → leap: {leap}, days: {days}, season: {season}")

