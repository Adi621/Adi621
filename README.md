# Tic Tac Toe – Python Console Game

This repository contains a Python implementation of the classic **Tic Tac Toe**
game played in the console.

The game supports:
- Two human players
- Human vs computer (with a simple intelligent strategy)

---

## Features

- Interactive console-based interface
- Clear visual representation of the game board
- Input validation and error handling
- Scoreboard tracking across multiple games
- Computer opponent with basic strategy:
  - Prioritizes winning moves
  - Blocks opponent’s winning moves
  - Prefers corner positions in early game

---

## Game Modes

### 1️⃣ Player vs Player
- Two human players take turns
- Players can choose to play as **X** or **O**
- Scoreboard is updated after each game

### 2️⃣ Player vs Computer
- Human player competes against the computer
- Computer uses a rule-based “smart move” strategy
- Game continues until the player chooses to quit

---

## How to Play

1. Run the script:
   ```bash
   python tic_tac_toe.py


## Choose game mode:

Press 1 to play against a friend

Press any other key to play against the computer

Choose your symbol (X or O)


## Enter a number from 1 to 9 to place your move:
    7 | 8 | 9
    ---------
    4 | 5 | 6
    ---------
    1 | 2 | 3


## The game announces:

Win

Draw

Updated scoreboard

## Code Structure

print_tic_tac_toe() – Displays the board

check_win() – Checks all winning combinations

check_draw() – Detects draw condition

single_game() – Player vs player logic

single_gameComputer() – Player vs computer logic

smartmove() – Computer move selection logic

## Technologies Used

Python

Standard library (random)

Console input/output

## Design Notes

The board is represented as a list of 9 elements

Player positions are tracked using dictionaries

Computer logic uses rule-based decision making
(not Minimax, but deterministic and readable)

