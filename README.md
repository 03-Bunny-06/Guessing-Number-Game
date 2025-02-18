# Guessing Number Game

## Project Description

This Python program is an interactive **Guessing Number Game** that challenges players to guess a randomly generated number based on difficulty levels. It provides feedback after every guess to guide the player toward the correct answer.

## Features

### Three Difficulty Levels:
- **Easy:** Single-digit numbers (1–10).
- **Medium:** Double-digit numbers (10–99).
- **Hard:** Triple-digit numbers (100–999).

### User Guidance:
- Indicates whether the guessed number is **higher** or **lower** than the correct answer.
- Tracks the number of attempts taken to guess correctly.

### Replayable:
- The program ends after a correct guess but can be restarted by rerunning the script.

## How to Play

1. Run the program in a **Python interpreter**.
2. Select a difficulty level:
   - Enter **1** for Easy.
   - Enter **2** for Medium.
   - Enter **3** for Hard.
3. Input your guesses:
   - The program will provide feedback if your guess is too high or too low.
4. Continue guessing until you get the correct number.
5. The program will display the total number of **attempts taken** to guess correctly.

## Example Gameplay

### Start:
```
Welcome to the Guessing Number Game.

Easy - (guessing number is single digit)
Medium - (guessing number is double digit)
Hard - (guessing number is triple digit)
Enter the choice(1/2/3): 2
```

### Gameplay:
```
Enter your guessing number: 45
The number you have guessed is 'HIGHER THAN' the answer.

Enter your guessing number: 30
The number you have guessed is 'LOWER THAN' the answer.

Enter your guessing number: 35
Your guessing number 35 is correct!!

You took 3 guesses to find the right answer.
```

## Requirements

- Python **3.x**
- No external libraries required
