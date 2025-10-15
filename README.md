Rock, Paper, Scissors (RPS) with Intelligent AI
An interactive console game (CLI) created in Python, equipped with adaptive AI that learns the player's movement patterns.

-> Game Features
    Game Modes: Play a single round or enter Best of 3 or Best of 5 mode.
    Adaptive AI (Intelligent Computer): The computer analyses your move history (detects sequences and patterns, e.g. (Rock, Paper) -> Scissors) and predicts your next move to beat you.
    Session Statistics: Track your overall win rate and analyse your most frequently chosen moves.
    Unit Tests: The game logic and AI module are covered by unit tests using the unittest module.

-> Requirements
    The game only requires Python 3 to be installed.

-> Installation and Launch
    Clone the Repository: git clone https://github.com/Magdaa1/stonepaperscissors.git
    cd stonepaperscissors

-> Run the Main File: stonepaperscissors.py

-> User Manual
After launching the game, you will see the menu:

Welcome to the game: ROCK, PAPER, SCISSORS
1. Play one round
2. Best of 3 (up to 3 wins)
3. Best of 5 (up to 5 wins)
4. Statistics
5. Exit
Select options (1-5):
Select 1, 2 or 3 to start the game.

During the round, enter your move: rock, paper or scissors.

Select 4 to check your results from the current session and see how often you use each move.

->  How AI Works (For the Curious)
The AI module does not play randomly. It uses a Markov chain of order 2 to analyse sequences:
    It remembers the entire history of the player's moves.
    It identifies the last two moves you played (e.g. (Paper, Rock)).
    It searches the entire history for what happened in the past after the same pattern (Paper, Rock).
    It selects the move that most often followed this pattern (this is the player's predicted move).
The AI plays a move that beats this predicted move.


-> Unit Tests
    The project includes unit tests (unittest) in the test_stonepaperscissors.py file, which guarantee the correctness of the logic:
    Rules of the Game: Checking whether Rock actually beats Scissors in all possible combinations.
    AI Logic: Checking whether the AI correctly identifies and responds to simple, repetitive patterns of player moves.
-> To run the tests, use: python -m unittest test_stonepaperscissors.py
