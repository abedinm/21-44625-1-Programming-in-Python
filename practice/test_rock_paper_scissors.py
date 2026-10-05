import pytest
from rock_paper_scissors import decide_winner, normalize_choice


@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("scissors", "paper", "win"),
        ("rock", "paper", "lose"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("rock", "rock", "draw"),
        ("paper", "paper", "draw"),
        ("scissors", "scissors", "draw"),
    ],
)
def test_decide_winner(player, computer, expected):
    assert decide_winner(player, computer) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("rock", "rock"),
        (" Paper ", "paper"),
        ("SCISSORS", "scissors"),
        ("r", "rock"),
        ("P", "paper"),
        ("s", "scissors"),
        ("lizard", None),
        ("", None),
    ],
)
def test_normalize_choice(text, expected):
    assert normalize_choice(text) == expected
