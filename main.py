import random


def set_difficulty():
    # Determines # of lives
    level = (input("Choose a difficulty. Type 'easy' or 'hard': ").lower())
    if level == "easy":
        return EASY_LIVES
    else:
        return HARD_LIVES


def check_answer(guess, answer, turns):
    # Compares your guess to the answer
    # Keeps track of the number of turns
    if guess != answer:
        if guess > number_to_guess:
            print("Your guess is too high try again!")
            return turns - 1
        else:
            print("Your guess is too low try again!")
            return turns - 1
    else:
        print("You guessed the number! You win")


def guess_the_number():
    # Logic of the game
    # Loops by taking in guesses
    lives = set_difficulty()
    user_guess = 0
    print("Welcome to the Number Guessing Game! \n"
          "I'm thinking of a number between 1 and 100. ")
    while user_guess != number_to_guess:
        print(f"You have {lives} attempts remaining to guess the number.")

        user_guess = int(input("\nGuess the number: "))
        lives = check_answer(user_guess, number_to_guess, lives)
        if lives == 0:
            print("You ran out of lives, You loose!")
            break


# DRIVER CODE
EASY_LIVES = 10
HARD_LIVES = 5
number_to_guess = random.randint(1, 100)
# print(number_to_guess) # Print number_to_guess for debugging
guess_the_number()
