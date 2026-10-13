import random


def run():
    lower_number, higher_number, attempt = 0, 100, 10
    secret_num = random.randint(0, 100)
    game_win = False
    print("====================\n"
          "Number guessing game\n"
          "====================")
    while attempt > 0 or game_win==True:


        try:
            guess = int(input(f"Guess the secret number between {lower_number} and {higher_number} : "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if lower_number > guess or guess > higher_number:
            print("Wrong entry, try again")
            continue
        elif guess > secret_num:
            print("the secret number is lower than " + str(guess))
            higher_number = guess
            attempt -= 1
        elif guess < secret_num:
            print("the secret number is higher than " + str(guess))
            lower_number = guess
            attempt -= 1

        else:
            game_win=True

    if attempt == 0:
        print("you loose")
    elif game_win==True:
        print('You won the game !')

if __name__ == "__main__":
    run()