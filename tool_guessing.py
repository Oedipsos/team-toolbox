import random


def run():
    lower_number, higher_number, attempt = 0, 100, 10
    secret_num = random.randint(0, 100)
    print("====================\n"
          "Number guessing game\n"
          "====================")
    while attempt > 0:

        guess = int(input(f"Guess the secret number between {lower_number} and {higher_number} : "))

        if lower_number > guess > higher_number:
            print("Wrong entry, try again")
        if guess > secret_num:
            print("the secret number is lower than " + str(guess))
            higher_number = guess
            attempt -= 1
        elif guess < secret_num:
            print("the secret number is higher than " + str(guess))
            lower_number = guess
            attempt -= 1

        else:
            print("You won the game !")
            break
    if attempt == 0:
        print("you loose")

run()

if __name__ == "__main__":
    run()