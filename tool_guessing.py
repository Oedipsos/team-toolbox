import random


def run():

    attempts = 10
    lower_number, higher_number = 0, 100
    secret_num = random.randint(0, 100)
    
    print("====================\n"
          "Number guessing game\n"
          "====================")
    
    while attempts > 0:
        try:
            guess = int(input(
                f"Guess the secret number between "
                f"{lower_number} and {higher_number} : "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if lower_number >= guess or guess >= higher_number:
            print("Wrong entry, try again")
            continue
        
        if guess > secret_num:

            print("The secret number is lower than " + str(guess))
            higher_number = guess
            attempts -= 1
            print(f"attempts left : {attempts}")

        elif guess < secret_num:

            print("The secret number is higher than " + str(guess))
            lower_number = guess
            attempts -= 1
            print(f"attempts left : {attempts}")

        else:
            print(f"Congratulations, you won the game !"
                  f"attempts left : {attempts}")
            break
    else: 
        print("You loose")


if __name__ == "__main__":
    run()
