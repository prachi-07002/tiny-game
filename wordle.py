"""Tiny Game: Wordle in the terminal.

Guess the 5-letter word in 6 tries.
  🟩  right letter, right spot
  🟨  right letter, wrong spot
  ⬜  letter not in the word

Usage:
    python wordle.py
"""

import random

WORDS = [
    "crane", "slate", "brave", "light", "music", "plant", "ocean",
    "happy", "dream", "flame", "stone", "bread", "cloud", "dance",
    "eagle", "frost", "grape", "heart", "ivory", "juice", "koala",
    "lemon", "mango", "night", "olive", "piano", "queen", "river",
    "sugar", "tiger", "ultra", "vivid", "whale", "young", "zebra",
    "apple", "beach", "candy", "delta", "ember",
]

GREEN, YELLOW, GRAY, RESET = "\033[92m", "\033[93m", "\033[90m", "\033[0m"


def feedback(guess, answer):
    """Per-letter feedback: 'G' (green), 'Y' (yellow), '-' (gray).

    Two passes so repeated letters are scored correctly: greens first,
    then yellows only for letters the answer still has unmatched.
    """
    result = ["-"] * 5
    remaining = list(answer)
    for i, (g, a) in enumerate(zip(guess, answer)):
        if g == a:
            result[i] = "G"
            remaining.remove(g)
    for i, g in enumerate(guess):
        if result[i] == "-" and g in remaining:
            result[i] = "Y"
            remaining.remove(g)
    return "".join(result)


def render(guess, marks):
    colors = {"G": GREEN, "Y": YELLOW, "-": GRAY}
    return " ".join(f"{colors[m]}{ch.upper()}{RESET}"
                    for ch, m in zip(guess, marks))


def play_round(answer):
    print("\nGuess the 5-letter word! You have 6 tries.")
    for attempt in range(1, 7):
        try:
            guess = input(f"Try {attempt}/6: ").strip().lower()
        except EOFError:
            print("\nGame over. The word was:", answer.upper())
            return False
        if len(guess) != 5 or not guess.isalpha():
            print("  Must be a 5-letter word.")
            continue
        marks = feedback(guess, answer)
        print(" ", render(guess, marks))
        if marks == "GGGGG":
            print(f"🎉 You got it in {attempt}!")
            return True
    print(f"Out of tries! The word was: {answer.upper()}")
    return False


def main():
    print("=== WORDLE ===")
    while True:
        play_round(random.choice(WORDS))
        try:
            again = input("\nPlay again? (y/n): ").strip().lower()
        except EOFError:
            break
        if again != "y":
            break
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
