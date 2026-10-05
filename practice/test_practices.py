import pytest
from p01_greeting import age_this_year
from p02_calculator import calculate, power
from p03_temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from p04_string_basics import count_vowels, is_palindrome, reverse
from p05_even_odd import parity, sign
from p06_largest_of_three import largest_of_three
from p07_grade import letter_grade
from p08_triangle import triangle_type
from p09_fizzbuzz import fizzbuzz
from p10_guess_the_number import check_guess


def test_age_this_year():
    assert age_this_year(2001, 2026) == 25


def test_calculate():
    assert calculate(7, 2) == {"+": 9, "-": 5, "*": 14, "/": 3.5, "//": 3, "%": 1, "**": 49}


def test_calculate_divide_by_zero_is_undefined():
    results = calculate(5, 0)
    assert results["/"] is None
    assert results["//"] is None
    assert results["%"] is None
    assert results["+"] == 5


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(2, 10, 1024), (-2, 3, -8), (0, 0, 1), (0, -1, None), (-8, 0.5, None)],
)
def test_power(a, b, expected):
    assert power(a, b) == expected


@pytest.mark.parametrize(("celsius", "fahrenheit"), [(0, 32), (100, 212), (37, 98.6), (-40, -40)])
def test_temperature(celsius, fahrenheit):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(fahrenheit)
    assert fahrenheit_to_celsius(fahrenheit) == pytest.approx(celsius)


def test_strings():
    assert reverse("Python") == "nohtyP"
    assert count_vowels("Programming") == 3
    assert is_palindrome("Racecar")
    assert is_palindrome("Never odd or even")
    assert not is_palindrome("Python")


@pytest.mark.parametrize(
    ("number", "expected_parity", "expected_sign"),
    [(4, "even", "positive"), (-7, "odd", "negative"), (0, "even", "zero")],
)
def test_even_odd(number, expected_parity, expected_sign):
    assert parity(number) == expected_parity
    assert sign(number) == expected_sign


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [((1, 2, 3), 3), ((3, 2, 1), 3), ((2, 3, 1), 3), ((5, 5, 1), 5), ((-1, -5, -3), -1)],
)
def test_largest_of_three(numbers, expected):
    assert largest_of_three(*numbers) == expected


@pytest.mark.parametrize(
    ("score", "grade"),
    [(100, "A"), (90, "A"), (89.9, "B"), (80, "B"), (70, "C"), (60, "D"), (59.9, "F"), (0, "F")],
)
def test_letter_grade(score, grade):
    assert letter_grade(score) == grade


@pytest.mark.parametrize("score", [-1, 100.5])
def test_letter_grade_rejects_out_of_range(score):
    with pytest.raises(ValueError):
        letter_grade(score)


@pytest.mark.parametrize(
    ("sides", "expected"),
    [
        ((3, 3, 3), "equilateral"),
        ((3, 3, 5), "isosceles"),
        ((3, 4, 5), "scalene"),
        ((1, 2, 3), "not a triangle"),
        ((0, 1, 1), "not a triangle"),
        ((1, 10, 2), "not a triangle"),
    ],
)
def test_triangle_type(sides, expected):
    assert triangle_type(*sides) == expected


@pytest.mark.parametrize(
    ("number", "expected"),
    [(1, "1"), (3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz"), (30, "FizzBuzz"), (7, "7")],
)
def test_fizzbuzz(number, expected):
    assert fizzbuzz(number) == expected


def test_check_guess():
    assert check_guess(10, 50) == "higher"
    assert check_guess(60, 50) == "lower"
    assert check_guess(50, 50) == "correct"
