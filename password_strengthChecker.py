import re

# Function to check password strength
def check_password_strength(password):
    # Check the length of the password
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Check for at least one uppercase letter
    if not re.search("[A-Z]", password):
        return "Weak: Password should contain at least one uppercase letter."

    # Check for at least one lowercase letter
    if not re.search("[a-z]", password):
        return "Weak: Password should contain at least one lowercase letter."

    # Check for at least one digit
    if not re.search("[0-9]", password):
        return "Weak: Password should contain at least one number."

    # Check for special characters
    if not re.search("[@#$%^&+=]", password):
        return "Weak: Password should contain at least one special character."

    # If all conditions are met, the password is strong
    return "Strong: Password meets all the requirements."

# Main function to get user input and display the result
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)
