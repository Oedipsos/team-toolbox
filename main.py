import tool_wordstat as ws


def show_menu():
    """Display the list of available tools."""
    print()
    print("=== Team Toolbox ===")
    print("0. Quit")
    print("1. Word statistics tool")


def main():
    print('Welcome to the Team Toolbox! Choose a tool in the menu.')
    # Ask the user for a choice until they decide to quit.
    
    while True:
        show_menu()
        choice = input("Your choice: ")
        choice = choice.strip()
        match choice:
            case "0":
                print("Goodbye!")
                break
            case "1":
                print("Running Word stats tool...")
                print()
                ws.run()
            case _:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
