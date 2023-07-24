import sys

def main():
    argv = sys.argv[1:]
    num_args = len(argv)

    print(f"Number of argument(s): {num_args}", end=' ')
    if num_args == 0:
        print(".",  end='\n')
    elif num_args == 1:
        print("argument:", end='\n')
        print(f"1: {argv[0]}")
    else:
        print("arguments:", end='\n')
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
