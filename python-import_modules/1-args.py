import sys

def main():
    argv_length = len(sys.argv) - 1
    arguments = sys.argv[1:]

    print(f"Number of argument{'s' if argv_length != 1 else ''}: {argv_length}", end='')
    print(f":{'.' if argv_length == 0 else ''}")

    if argv_length > 0:
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
