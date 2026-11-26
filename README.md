# Rock Paper Scissors

A Rock-Paper-Scissors AI from the freeCodeCamp Machine Learning with Python curriculum. The `player` function in `RPS.py` has no fixed strategy of its own — it maintains a running history of the opponent's moves, scores how well each of four known bot strategies (Quincy, Kris, Mrugesh, Abbey) would have predicted that history so far, and counters whatever the best-matching strategy predicts next.

## Problem and objective

The freeCodeCamp challenge provides four fixed opponent bots and requires a `player` function that wins at least 60% of 1,000 games against each one.

## Technologies and libraries used

Python standard library only (`random`, `unittest`) — no third-party dependencies.

## Algorithm

`player()` in `RPS.py`:
1. Tracks `opponent_history` and its own `my_history` across the match, resetting both when `prev_play == ""` (start of a new match).
2. Defines a local copy of each bot's prediction logic (Quincy's fixed cycle, Kris's counter-last-move, Mrugesh's most-frequent-of-last-10, Abbey's Markov pair-frequency).
3. Replays the opponent's actual history against each of the four predictors and tallies how many moves each predictor would have gotten right.
4. Picks the best-scoring predictor, uses it to predict the opponent's *next* move, and plays the counter to that prediction.
5. Falls back to a random move only for the very first move of a match, when there is no history yet.

## Implementation details

- `RPS_game.py` (unmodified, per the challenge rules) implements the four opponent bots and the `play()` match runner.
- `main.py` runs 1,000-game matches against each bot and then runs the official `test_module.py` suite.
- `test_module.py` asserts a ≥60% win rate against each of the four bots over 1,000 games.

## Training and evaluation results

Measured by running `python main.py` in this repo (1,000 games per opponent):

| Opponent | Player win rate | Result |
|---|---|---|
| Quincy | 100.0% | ✅ pass (≥60%) |
| Kris | 99.8–99.9% | ✅ pass (≥60%) |
| Mrugesh | 99.7% | ✅ pass (≥60%) |
| Abbey | 87.5% | ✅ pass (≥60%) |

All 4 tests in `test_module.py` pass (`OK`, exit code 0).

## How to install and run

```bash
git clone https://github.com/jayahareeswarreddy/boilerplate-rock-paper-scissors.git
cd boilerplate-rock-paper-scissors
python main.py
```

No `pip install` is required — the project only uses the Python standard library.

## freeCodeCamp project reference

https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

## Future improvements

- Track per-opponent confidence and blend predictions instead of always committing fully to the single best-scoring bot.
- Add a human-playable CLI mode using the existing `human` player in `RPS_game.py`.
- Benchmark against a wider set of adversarial strategies beyond the four bundled bots.
