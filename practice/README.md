# Practice

Small programs for practising the basics. Each file starts with its task and an
example run. Try writing it yourself before reading the solution below the task.

| # | File | Practises |
|---|------|-----------|
| 01 | [p01_greeting.py](p01_greeting.py) | `input()`, `int()`, variables, f-strings |
| 02 | [p02_calculator.py](p02_calculator.py) | arithmetic operators, avoiding division by zero |
| 03 | [p03_temperature.py](p03_temperature.py) | formulas, `if` / `elif` / `else` |
| 04 | [p04_string_basics.py](p04_string_basics.py) | string methods, slicing, palindromes |
| 05 | [p05_even_odd.py](p05_even_odd.py) | `%`, `if` / `else` |
| 06 | [p06_largest_of_three.py](p06_largest_of_three.py) | comparisons, `and` |
| 07 | [p07_grade.py](p07_grade.py) | `if` / `elif` chains, input range checks |
| 08 | [p08_triangle.py](p08_triangle.py) | nested conditions |
| 09 | [p09_fizzbuzz.py](p09_fizzbuzz.py) | `for` loops, `range()` |
| 10 | [p10_guess_the_number.py](p10_guess_the_number.py) | `while` loops, `random` |
| — | [rock_paper_scissors.py](rock_paper_scissors.py) | a full game: loops, dictionaries, `random` |

Run one:

```bash
uv run python practice/p02_calculator.py
```

Check them all:

```bash
uv run pytest practice
```

To practise one again: delete the body of a function, write your own version,
and run the tests until they pass.
