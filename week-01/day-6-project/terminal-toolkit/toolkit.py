# toolkit.py - terminal-toolkit: a tiny multi-tool CLI

APP_NAME = "terminal-toolkit"
VERSION = "0.1.0"
LINE = "=" * 40

def main():
    print(LINE)
    print(f"{APP_NAME + ' v' + VERSION:^40}")
    print(LINE)

    while True:
        print()
        print("[1] Unit converter")
        print("[2] Tip calculator")
        print("[3] Text stats")
        print("[q] Quit")
        choice = input("> ").strip().lower()

        if choice == "1":
            print("-- Unit converter --")
            print("Options: c2f, f2c, km2mi, mi2km, kg2lb, lb2kg")
            kind = input("Conversion type: ").strip().lower()
            try:
                value = float(input("Value to convert: "))
                if kind == "c2f":
                    result = value * 9 / 5 + 32
                    print(f"{value:.2f} C = {result:.2f} F")
                elif kind == "f2c":
                    result = (value - 32) * 5 / 9
                    print(f"{value:.2f} F = {result:.2f} C")
                elif kind == "km2mi":
                    result = value * 0.621371
                    print(f"{value:.2f} km = {result:.2f} mi")
                elif kind == "mi2km":
                    result = value / 0.621371
                    print(f"{value:.2f} mi = {result:.2f} km")
                elif kind == "kg2lb":
                    result = value * 2.20462
                    print(f"{value:.2f} kg = {result:.2f} lb")
                elif kind == "lb2kg":
                    result = value / 2.20462
                    print(f"{value:.2f} lb = {result:.2f} kg")
                else:
                    print(f"Unknown conversion: {kind}")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "2":
            print("-- Tip calculator --")
            try:
                bill = float(input("Bill amount: "))
                tip_percent = float(input("Tip percentage (e.g. 15): "))
                people = int(input("Number of people: "))

                tip_amount = bill * (tip_percent / 100)
                total = bill + tip_amount
                per_person = total / people

                print("-" * 20)
                print(f"Tip: ${tip_amount:.2f}")
                print(f"Total: ${total:.2f}")
                print(f"Each person pays: ${per_person:.2f}")
                print("-" * 20)
            except ValueError:
                print("Error: Please enter valid numbers.")
            except ZeroDivisionError:
                print("Error: Number of people must be greater than zero.")
            

        elif choice == "3":
            print("-- Text stats --")
            text = input("Enter your text: ").strip()
            if not text:
                print("Error: The text cannot be empty.")
            else:
                char_count = len(text)
                char_count_no_spaces = len(text.replace(" ", ""))
                word_count = len(text.split())

                print(f"Characters (with spaces): {char_count}")
                print(f"Characters (no spaces):   {char_count_no_spaces}")
                print(f"Words:                    {word_count}")

        elif choice == "q":
            print("Goodbye from terminal-toolkit. Keep shipping!")
            break

        else:
            print(f"'{choice}' is not a valid option.")

if __name__ == "__main__":
    main()

