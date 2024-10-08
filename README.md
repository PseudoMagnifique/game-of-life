# Game of Life

Implementation of the game of life in Python.

## Rules

The game takes place in a grid, where every cell can either be alive or dead. You create the initial configuration and each new generation is determined by the following rules:
1. If a cell has 2 alive neighbours, its state remains the same.
2. If a dead cell has 3 alive neighbours, it becomes alive. If the cell was already alive, its state remains the same.
3. If a cell has another amount of alive neighbours, it dies: 0 or 1 by underpopulation, 4 or more by overpopulation.

The neighbours of a cell are the 8 cells around it.

## Usage

1. Clone the repo
`git clone https://github.com/PseudoMagnifique/game-of-life`
2. Launch `main.py` with `python3 path/to/main.py (--rows n) (--columns m) (--zqsd)`, where the parameters between parenthesis are optional.
   - The `n` and `m` parameters represent the number of rows and columns respectively. Their default value being 20, the grid is 20x20 if no `n` and `m` parameters are specified.
   - The `--rows` and `--columns` flags can be replaced with `-r` and `-c` respectively.
   - Use `--zqsd` if you want to navigate in the grid using the zqsd keys instead of the default wasd.
3. Use the wasd keys on your keyboard to move from one cell to another, tap `x` to make a dead cell alive or kill a living cell.
4. Once you're done and satisfied with the initial configuration, tap `<Enter>` and watch the game unfold.

*Bonus:* When the commands are given and you are asked to tap `<Enter>` to continue, tapping `show w` or `show c` will give you the links to the (correct, I hope) parts of the license as stated in the part of the license printed in the terminal.

Enjoy!