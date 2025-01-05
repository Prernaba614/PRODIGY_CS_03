import re

def assess_password_strength(password):
    # Initialize criteria flags
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[@$!%*?&]', password) is not None

    # Count the number of criteria met
    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    # Determine strength based on criteria met
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lower_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not special_criteria:
        feedback.append("Password should contain at least one special character (e.g., @$!%*?&).")

    return strength, feedback

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Feedback:")
        for message in feedback:
            print(f"- {message}")
    else:
        print("Your password meets all strength criteria!")

if __name__ == "__main__":
    main()