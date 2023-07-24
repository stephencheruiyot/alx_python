import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name from the arguments
    num_arguments = len(argv)
    if num_arguments == 0:
        print("0 argument.")
    else:
        print(f"{num_arguments} {'argument' if num_arguments == 1 else 'arguments'}:")

        for i, arg in enumerate(argv, 1):
            print(f"{i}: {arg}")
if __name__ == "__main__":
    main()
