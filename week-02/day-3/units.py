"""Unit conversion library containing pure functions for temperature, distance, and weight."""


def c_to_f(c: float) -> float:
    """Converts Celsius to Fahrenheit.

    Args:
        c (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return c * 9 / 5 + 32


def f_to_c(f: float) -> float:
    """Converts Fahrenheit to Celsius.

    Args:
        f (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    return (f - 32) * 5 / 9


def km_to_mi(km: float) -> float:
    """Converts kilometers to miles.

    Args:
        km (float): Distance in kilometers.

    Returns:
        float: Distance in miles.
    """
    return km * 0.621371


def mi_to_km(mi: float) -> float:
    """Converts miles to kilometers.

    Args:
        mi (float): Distance in miles.

    Returns:
        float: Distance in kilometers.
    """
    return mi * 1.60934


def kg_to_lb(kg: float) -> float:
    """Converts kilograms to pounds.

    Args:
        kg (float): Weight in kilograms.

    Returns:
        float: Weight in pounds.
    """
    return kg * 2.20462


def lb_to_kg(lb: float) -> float:
    """Converts pounds to kilograms.

    Args:
        lb (float): Weight in pounds.

    Returns:
        float: Weight in kilograms.
    """
    return lb * 0.453592


def convert(value: float, kind: str) -> float | None:
    """Dispatcher function to convert values based on the specified kind.

    Args:
        value (float): The numeric value to convert.
        kind (str): The type of conversion (e.g., 'c2f', 'f2c', 'km2mi', 'mi2km',
          'kg2lb', 'lb2kg').

    Returns:
        float | None: The converted value, or None if the kind is unknown.
    """
    match kind:
        case "c2f":
            return c_to_f(value)
        case "f2c":
            return f_to_c(value)
        case "km2mi":
            return km_to_mi(value)
        case "mi2km":
            return mi_to_km(value)
        case "kg2lb":
            return kg_to_lb(value)
        case "lb2kg":
            return lb_to_kg(value)
        case _:
            return None


if __name__ == "__main__":
    assert round(c_to_f(100), 2) == 212.0
    assert round(c_to_f(0), 2) == 32.0

    assert round(f_to_c(-40), 2) == -40.0
    assert round(f_to_c(212), 2) == 100.0

    assert round(km_to_mi(10), 2) == 6.21
    assert round(mi_to_km(6.21371), 2) == 10.0

    assert round(kg_to_lb(1), 2) == 2.2
    assert round(lb_to_kg(2.20462), 2) == 1.0

    assert round(convert(100, "c2f"), 2) == 212.0
    assert round(convert(-40, "f2c"), 2) == -40.0
    assert convert(1, "unknown") is None
    assert convert(50, "invalid_kind") is None

    print("units ok")

