# Tic Tac Toe Game

Welcome to the Tic Tac Toe game implemented in Python! This simple command-line game allows two players to take turns placing their symbols (X or O) on a 3x3 grid with the goal of getting three in a row. The game ends when either one player achieves three in a row or the grid is full without any player getting three in a row, resulting in a tie.

## How to Play

Clone the repository to your local machine.
Navigate to the directory containing the game files.
Run the tictactoe.py file using Python.
Follow the on-screen instructions to play the game.
Alternate turns between players, entering the row and column where you want to place your symbol.
The game will automatically determine if a player has won or if the game has ended in a tie.

## Features

Command-line interface: Play the game directly in your terminal without the need for any graphical interface.
Game board visualization: The game board is displayed as a 3x3 grid, making it easy to visualize the current state of the game.
Win and tie detection: The game logic automatically checks for winning combinations and detects when the game has ended in a tie.
Player input validation: Player moves are validated to ensure they are within the bounds of the game board and on an empty square.
Clear and concise code: The game logic is implemented using Python's built-in data structures and control flow statements, making it easy to understand and modify.

## Game Logic

The game logic is divided into several functions:

 - print_board(): Prints the current state of the game board.   
 - player_move(): Handles player moves by prompting for input and updating   the game board. 
 -  check_win(): Checks if any player has achieved three in a row.  
 - check_tie(): Checks if the game has ended in a tie. 
 -  Main game loop: Alternates between players, allowing them to
   make moves until the game ends.

## Testing and Debugging

The game has been thoroughly tested to ensure that it functions correctly in various scenarios. However, if you encounter any issues while playing the game, feel free to report them on GitHub. We appreciate your feedback and will address any bugs as soon as possible.

## Enjoy the Game!

We hope you enjoy playing Tic Tac Toe with your friends or family using this simple command-line implementation. Have fun strategizing and trying to outwit your opponent! If you have any suggestions for improvements or new features, don't hesitate to let us know. Happy gaming!
