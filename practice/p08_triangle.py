"""Practice 08 - nested conditions.

Task: read three side lengths. If they can't form a triangle, say so.
Otherwise say whether it is equilateral (3 equal sides), isosceles
(2 equal sides) or scalene (no equal sides).

Three sides form a triangle only if all are positive and any two
sides together are longer than the third.

Example:
    Side a: 3
    Side b: 4
    Side c: 5
    That is a scalene triangle.

Run:  uv run python practice/p08_triangle.py
"""


def is_triangle(a: float, b: float, c: float) -> bool:
    all_positive = a > 0 and b > 0 and c > 0
    return all_positive and a + b > c and a + c > b and b + c > a


def triangle_type(a: float, b: float, c: float) -> str:
    if not is_triangle(a, b, c):
        return "not a triangle"

    if a == b == c:
        return "equilateral"
    elif a == b or b == c or c == a:
        return "isosceles"
    else:
        return "scalene"


def main() -> None:
    a = float(input("Side a: "))
    b = float(input("Side b: "))
    c = float(input("Side c: "))

    kind = triangle_type(a, b, c)
    if kind == "not a triangle":
        print("Those sides can't form a triangle.")
    else:
        print(f"That is a {kind} triangle.")


if __name__ == "__main__":
    main()
