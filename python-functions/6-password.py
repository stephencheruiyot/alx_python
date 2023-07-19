def validate_password(password):
    # Check password length
    if len(password) < 8:
        return False

    # Check if password contains at least one uppercase letter, one lowercase letter, and one digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if not (has_uppercase and has_lowercase and has_digit):
        return False

    # Check if password contains spaces
    if ' ' in password:
        return False

    # All checks passed
    return True

# Example usage:
password1 = "StrongP@ssword123"
password2 = "weakpass"
password3 = "Password with spaces"

print(validate_password(password1))  # True
print(validate_password(password2))  # False
print(validate_password(password3))  # False
