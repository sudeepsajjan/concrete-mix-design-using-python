import os


def select_program():
    while True:
        print("Select a program to run:")
        print("1. 1982.py")
        print("2. 2009.py")
        print("3. 2019.py")
        choice = input("Enter the program number (1/2/3): ").strip()

        if choice in {'1', '2', '3'}:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def run_program(program_number):
    program_files = ["1982.py", "2009.py", "2019.py"]
    if 1 <= int(program_number) <= 3:
        os.system(
            f"code {program_files[int(program_number) - 1]} && python {program_files[int(program_number) - 1]}")
    else:
        print("Program not found.")


if __name__ == "__main__":
    selected_program = select_program()
    run_program(selected_program)
