"""Terminal Toolkit project refactored into pure and modular functions."""


def show_menu() -> None:
    """Displays the main menu options to the user."""
    print("\n--- Terminal Toolkit ---")
    print("1. Converter")
    print("2. Tip Calculator")
    print("3. Text Stats")
    print("4. Exit")


def ask_float(prompt: str) -> float:
    """Prompts the user for a floating-point number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def ask_int(prompt: str, low: int, high: int) -> int:
    """Prompts the user for an integer within a specific range."""
    while True:
        try:
            val = int(input(prompt))
            if low <= val <= high:
                return val
            print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def run_converter() -> None:
    """Handles the unit conversion feature."""
    print("\n[Converter]")
    val = ask_float("Enter value to convert (C to F): ")
    result = val * 9 / 5 + 32
    print(f"Result: {result:.2f} °F")


def tip_breakdown(bill: float, percent: int, people: int) -> tuple[float, float, float] | None:
    """Calculates tip amount, total bill, and share per person.

    Pure function.
    """
    if people <= 0 or bill < 0:
        return None
    tip_amount = bill * (percent / 100)
    total_bill = bill + tip_amount
    per_person = total_bill / people
    return tip_amount, total_bill, per_person


def run_tip_calculator() -> None:
    """Handles the tip calculator feature."""
    print("\n[Tip Calculator]")
    bill = ask_float("Enter bill amount: ")
    percent = ask_int("Enter tip percentage (e.g., 10, 15, 20): ", 0, 100)
    people = ask_int("Enter number of people: ", 1, 1000)

    res = tip_breakdown(bill, percent, people)
    if res:
        tip, total, share = res
        print(f"Tip Amount: {tip:.2f}")
        print(f"Total Bill: {total:.2f}")
        print(f"Share Per Person: {share:.2f}")


def text_stats(text: str) -> dict[str, int]:
    """Analyzes text and returns statistics (char count, word count, etc.).

    Pure function.
    """
    words = text.split()
    return {
        "chars": len(text),
        "words": len(words),
    }


def run_text_stats() -> None:
    """Handles the text statistics feature."""
    print("\n[Text Stats]")
    text = input("Enter your text: ")
    stats = text_stats(text)
    print(f"Characters: {stats['chars']}")
    print(f"Words: {stats['words']}")


def main() -> None:
    """Main application loop."""
    while True:
        show_menu()
        choice = ask_int("Choose an option (1-4): ", 1, 4)
        if choice == 1:
            run_converter()
        elif choice == 2:
            run_tip_calculator()
        elif choice == 3:
            run_text_stats()
        elif choice == 4:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

