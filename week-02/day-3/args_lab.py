"""Receipt formatter module demonstrating *args and keyword-only arguments."""


def format_receipt(
    *items: float, tax_rate: float = 0.09, currency: str = "IRR"
) -> str:
    """Formats a multi-line receipt with subtotal, tax, and total.

    Args:
        *items (float): Variable number of item prices.
        tax_rate (float): Tax rate percentage (keyword-only).
        currency (str): Currency symbol (keyword-only).

    Returns:
        str: Formatted receipt string.
    """
    subtotal = sum(items)
    tax = subtotal * tax_rate
    total = subtotal + tax

    receipt_lines = [
        "--- Receipt ---",
        f"Subtotal: {subtotal:,.2f} {currency}",
        f"Tax ({tax_rate * 100}%): {tax:,.2f} {currency}",
        f"Total: {total:,.2f} {currency}",
    ]
    return "\n".join(receipt_lines)


if __name__ == "__main__":
    # Test 1: Normal receipt with multiple items
    r1 = format_receipt(100.0, 200.0, 300.0, tax_rate=0.1, currency="TTO")
    assert "Subtotal: 600.00 TTO" in r1

    # Test 2: Receipt with default parameters
    r2 = format_receipt(1000.0, 2000.0)
    assert "Subtotal: 3,000.00 IRR" in r2

    # Test 3: Empty items receipt
    r3 = format_receipt()
    assert "Subtotal: 0.00 IRR" in r3

    # Test 4: Custom tax rate and currency
    r4 = format_receipt(50.0, 50.0, tax_rate=0.05, currency="USD")
    assert "Total: 105.00 USD" in r4

    print("args_lab ok")

