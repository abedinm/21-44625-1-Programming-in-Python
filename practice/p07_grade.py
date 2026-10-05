"""Practice 07 - if/elif chains.

Task: read an exam score (0-100) and print the letter grade.
Reject scores outside 0-100 with a message instead of a grade.

    90-100 A    80-89 B    70-79 C    60-69 D    below 60 F

(Change the cut-offs to match your own course policy.)

Example:
    Score (0-100): 84.5
    Grade: B

Run:  uv run python practice/p07_grade.py
"""


def letter_grade(score: float) -> str:
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main() -> None:
    score = float(input("Score (0-100): "))
    if 0 <= score <= 100:
        print(f"Grade: {letter_grade(score)}")
    else:
        print("Please enter a score between 0 and 100.")


if __name__ == "__main__":
    main()
