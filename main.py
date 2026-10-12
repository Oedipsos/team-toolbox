import random


def show_menu():
    """Display the list of available tools."""
    print()
    print("=== Team Toolbox ===")
    print("0. Quit")
    print("2. Number guessing game")

def guessing_game():
    lower_number, higher_number, attempt = 0, 100, 10
    secret_num = random.randint(0, 100)
    while attempt > 0:
        print("====================\n"
              "Number guessing game\n"
              "====================")
        guess = int(input(f"Guess the secret number between {lower_number} and {higher_number} : "))
        if lower_number > guess > higher_number:
            print("Wrong entry, try again")
        if guess > secret_num:
            print("the secret number is lower than " + str(guess))
            higher_number = guess
            attempt -= 1
        elif guess < secret_num:
            print("the secret number is greater than " + str(guess))
            lower_number = guess
            attempt -= 1

        else:
            print("You won the game !")
            break
    if attempt == 0:
        print("you loose")
def main():
    print('Welcome to the Team Toolbox! Choose a tool in the menu.')
    """Ask the user for a choice until they decide to quit."""
    while True:
        show_menu()
        choice = input("Your choice: ")
        if choice == "0":
            print("Goodbye!")
            break
        if choice == "2":
            guessing_game()
        else:
            print("Invalid choice, try again.")


main()