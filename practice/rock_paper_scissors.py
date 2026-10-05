"""Rock, paper, scissors against the computer.

Run:  uv run python practice/rock_paper_scissors.py
"""

import random

CHOICES = ("rock", "paper", "scissors")
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}  # each key beats its value
SHORTCUTS = {"r": "rock", "p": "paper", "s": "scissors"}
QUIT_WORDS = ("q", "quit", "exit")


def normalize_choice(text: str) -> str | None:
    """Turn input like 'R', ' rock ' or 'Scissors' into a choice; None if it isn't one."""
    text = text.strip().lower()
    text = SHORTCUTS.get(text, text)
    return text if text in CHOICES else None


def decide_winner(player: str, computer: str) -> str:
    """Return 'win', 'lose' or 'draw' from the player's point of view."""
    if player == computer:
        return "draw"
    if BEATS[player] == computer:
        return "win"
    return "lose"


def format_score(score: dict[str, int]) -> str:
    return f"you {score['win']}, computer {score['lose']}, draws {score['draw']}"


def play() -> None:
    score = {"win": 0, "lose": 0, "draw": 0}
    print("Rock, paper, scissors! Type rock, paper or scissors (or r, p, s). Type q to quit.")

    while True:
        try:
            answer = input("\nYour move: ")
        except (EOFError, KeyboardInterrupt):  # Ctrl+D / Ctrl+C ends the game cleanly
            print()
            break

        if answer.strip().lower() in QUIT_WORDS:
            break

        player = normalize_choice(answer)
        if player is None:
            print("Please type rock, paper or scissors (or r, p, s).")
            continue

        computer = random.choice(CHOICES)
        result = decide_winner(player, computer)
        score[result] += 1

        print(f"You chose {player}, the computer chose {computer}.")
        if result == "win":
            print(f"You win! {player.capitalize()} beats {computer}.")
        elif result == "lose":
            print(f"You lose! {computer.capitalize()} beats {player}.")
        else:
            print("It's a draw.")
        print(f"Score: {format_score(score)}")

    print(f"\nFinal score: {format_score(score)}. Thanks for playing!")


if __name__ == "__main__":
    play()
