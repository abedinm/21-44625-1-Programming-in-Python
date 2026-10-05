"""Practice 03 - formulas and if/elif/else.

Task: convert a temperature between Celsius and Fahrenheit.
Ask which unit the user is converting from (C or F), then the value.

    F = C * 9 / 5 + 32
    C = (F - 32) * 5 / 9

Example:
    Convert from (C/F): c
    Temperature: 37
    37.0°C = 98.6°F

Run:  uv run python practice/p03_temperature.py
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def main() -> None:
    unit = input("Convert from (C/F): ").strip().upper()
    value = float(input("Temperature: "))

    if unit == "C":
        print(f"{value:.1f}°C = {celsius_to_fahrenheit(value):.1f}°F")
    elif unit == "F":
        print(f"{value:.1f}°F = {fahrenheit_to_celsius(value):.1f}°C")
    else:
        print("Please type C or F.")


if __name__ == "__main__":
    main()
