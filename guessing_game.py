from random import randint

answer = randint(1, 9)
while True:
    users_guess = int(input("Guess the number: "))

    if users_guess == answer:
        print(f"YOU WON!, the number was {answer}")
        break

    elif users_guess < answer:
        print("You guessed too low")

    elif users_guess > answer:
        print("You guessed too high")

