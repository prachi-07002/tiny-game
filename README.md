# Tiny Game: Wordle

A complete Wordle clone for the terminal — no dependencies, just Python.

## Usage

```bash
python wordle.py
```

Guess the 5-letter word in 6 tries. Green means right letter, right
spot; yellow means right letter, wrong spot; gray means not in the word.

## How it works

Feedback is scored in two passes (greens first, then yellows) so words
with repeated letters are handled correctly — the classic Wordle edge
case. The word list lives right in the file, so it's easy to extend.

## Ideas to extend

- Hard mode (green letters must be reused)
- A daily word mode with a shared puzzle
- Letter-frequency hints or a solver mode
