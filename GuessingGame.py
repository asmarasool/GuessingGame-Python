import random


def guess_game(x):
    random_number = random.randint(1, x)  # get us the  given range of random numbers
    guess = 0
    while guess != random_number:  # if what we iterate is not predefined then we use while loop
        guess = int(input(f"Guess a number between 0 and {x}: "))
        if guess < random_number:
            print("Sorry you guessed too low")
        elif guess > random_number:
            print("Sorry you guessed too high")

    print("Yay, you guessed the random number")
    print(guess)


guess_game(7)

def guess_computer(x):
    low = 1
    high = x
    user_feedback = ""
    while user_feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        user_feedback = input(f"Is {guess} too low or too high or correct?? ").lower()
        if user_feedback == "l":
            low = guess + 1
        elif user_feedback == "h":
            high = guess - 1
    print("Yay the computer guessed it right ")


guess_computer(15)

