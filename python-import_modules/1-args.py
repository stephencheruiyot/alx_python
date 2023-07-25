import sys

def print_arguments():
    arguments = sys.argv[1:]  # Exclude the script name itself from the arguments list
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    else:
        print(f"{num_arguments} {'argument' if num_arguments == 1 else 'arguments'}:")
        for i, arg in enumerate(arguments, 1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments()

