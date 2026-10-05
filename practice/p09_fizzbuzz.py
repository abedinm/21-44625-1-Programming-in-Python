"""Practice 09 - for loops.

Task: print the numbers from 1 to n, but print "Fizz" for multiples of 3,
"Buzz" for multiples of 5, and "FizzBuzz" for multiples of both.

Example:
    Count up to: 15
    1
    2
    Fizz
    4
    Buzz
    ...
    14
    FizzBuzz

Run:  uv run python practice/p09_fizzbuzz.py
"""


def fizzbuzz(number: int) -> str:
    if number % 15 == 0:  # check "both" first, or 15 would just print Fizz
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


def main() -> None:
    limit = int(input("Count up to: "))
    for number in range(1, limit + 1):
        print(fizzbuzz(number))


if __name__ == "__main__":
    main()
