def multiple_returns(sentence):
    if not sentence:  # Check if the sentence is empty
        return (0, None)  # Return a tuple with length 0 and None as the first character
    else:
        first_char = sentence[0]  # Get the first character of the string
    return (len(sentence), first_char)  # Return a tuple with the length of the string and its first character


