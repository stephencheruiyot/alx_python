def main():
    # Assign values to variables a and b
    a = 1
    b = 2

    # Import the add function from add_0.py
    import add_0
    result = add_0.add(a, b)

    # Print the result
    print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
    main()
