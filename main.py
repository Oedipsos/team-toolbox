import tool_guessing

def show_menu():
    """Display the list of available tools."""
    print()
    print("=== Team Toolbox ===")
    print("0. Quit")
    print("2.Guessing game")

def main():
    print('Welcome to the Team Toolbox! Choose a tool in the menu.')
    """Ask the user for a choice until they decide to quit."""
    while True:
        show_menu()
        choice = input("Your choice: ")
        if choice == "0":
            print("Goodbye!")
            break;
        elif choice=="2":
            tool_guessing.run()
        else:
            print("Invalid choice, try again.")


main()
