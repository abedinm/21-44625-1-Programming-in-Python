"""Practice 04 - strings.

Task: read a word or sentence and print facts about it: its length,
upper and lower case, reversed, first and last character, number of
vowels, and whether it is a palindrome (reads the same backwards,
ignoring case and spaces).

Example:
    Text: Never odd or even
    Length: 17
    Upper: NEVER ODD OR EVEN
    Lower: never odd or even
    Reversed: neve ro ddo reveN
    First / last character: N / n
    Vowels: 6
    Palindrome: yes

Run:  uv run python practice/p04_string_basics.py
"""

VOWELS = "aeiou"


def reverse(text: str) -> str:
    return text[::-1]


def count_vowels(text: str) -> int:
    return sum(1 for char in text.lower() if char in VOWELS)


def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == reverse(cleaned)


def main() -> None:
    text = input("Text: ")
    if not text:
        print("Please type something.")
        return

    print(f"Length: {len(text)}")
    print(f"Upper: {text.upper()}")
    print(f"Lower: {text.lower()}")
    print(f"Reversed: {reverse(text)}")
    print(f"First / last character: {text[0]} / {text[-1]}")
    print(f"Vowels: {count_vowels(text)}")
    print(f"Palindrome: {'yes' if is_palindrome(text) else 'no'}")


if __name__ == "__main__":
    main()
