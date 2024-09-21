# Global Variable for Paper
paper_level = 250


# Function to display the menu
def display_menu():
    print("\n--- Virtual Printer ---")
    print(f"Paper level: {paper_level} sheets")
    print("1. Print")
    print("2. Refill Paper")
    print("3. Exit")


# Function to print the pages
def print_pages():
    global paper_level
    try:
        pages = int(input("Enter the number of pages to print: "))
        if pages <= 0:
            print("Invalid input! Number of pages should be a positive number.")
            return
        if pages > paper_level:
            print(f"Not enough paper! The printer only has {paper_level} sheets left.")
        else:
            paper_level -= pages
            print(f"Printing {pages} pages... Done!")
    except ValueError:
        print("Please enter a valid number!")


# Function to refill the paper
def refill_paper():
    global paper_level
    try:
        refill_amount = int(input("Enter the number of sheets to refill (max 250): "))
        if refill_amount <= 0:
            print("Invalid input! You must add at least 1 sheet.")
            return
        if paper_level + refill_amount > 250:
            print(
                f"Cannot exceed 250 sheets. You can only add {250 - paper_level} more sheets."
            )
        else:
            paper_level += refill_amount
            print(f"Refilled {refill_amount} sheets of paper.")
    except ValueError:
        print("Please enter a valid number!")


# Function to run the program
def run():
    while True:
        display_menu()
        choice = input("Select an option (1-3): ")
        if choice == "1":
            print_pages()
        elif choice == "2":
            refill_paper()
        elif choice == "3":
            print("Exiting Virtual Printer. Goodbye!")
            break
        else:
            print("Invalid option! Please select a valid option.")


# This runs the main program
if __name__ == "__main__":
    run()
