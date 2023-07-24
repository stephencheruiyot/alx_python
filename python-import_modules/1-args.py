import sys

if __name__ == '__main__':
    argv = sys.argv[1:]
    num_args = len(argv)
    print(f"Number of argument(s): {num_args}")
    if num_args == 0:
        print(":")
    else:
        print(":")
        for i in range(num_args):
            print(f"{i+1}: {argv[i]}")