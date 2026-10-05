"""Practice 02 - arithmetic operators.

Task: read two numbers and show the result of every arithmetic operator:
    +   -   *   /   //   %   **
Results that aren't real numbers (like dividing by zero) must not crash
the program; show "undefined" instead.

Example:
    First number: 7
    Second number: 2
    7 + 2 = 9
    7 - 2 = 5
    7 * 2 = 14
    7 / 2 = 3.5
    7 // 2 = 3
    7 % 2 = 1
    7 ** 2 = 49

Run:  uv run python practice/p02_calculator.py
"""


def power(a: float, b: float) -> float | None:
    """a ** b, or None when it isn't a real number (0 to a negative power,
    or a negative number to a fractional power)."""
    if (a == 0 and b < 0) or (a < 0 and not b.is_integer()):
        return None
    return a**b


def calculate(a: float, b: float) -> dict[str, float | None]:
    """Every operator's result; None where the result is undefined."""
    return {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b if b != 0 else None,
        "//": a // b if b != 0 else None,
        "%": a % b if b != 0 else None,
        "**": power(a, b),
    }


def main() -> None:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    for operator, result in calculate(a, b).items():
        shown = "undefined" if result is None else f"{result:g}"
        print(f"{a:g} {operator} {b:g} = {shown}")


if __name__ == "__main__":
    main()
