import re

def assess_password_strength(password):
    strength = 0
    feedback = []
    
    # Check length
    if len(password) < 8:
        feedback.append("Password is too short, should be at least 8 characters.")
    else:
        strength += 1
    
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
    
    # Check for numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")
    
    # Check for special characters
    if re.search(r"[\W_]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character (e.g., @, #, $, etc.).")
    
    # Determine strength level
    if strength == 5:
        feedback.append("Password is very strong.")
    elif 3 <= strength < 5:
        feedback.append("Password is strong, but could be improved.")
    elif strength == 2:
        feedback.append("Password is weak.")
    else:
        feedback.append("Password is very weak.")
    
    return feedback

def main():
    # Get the password input from the user
    password = input("Enter your password to assess its strength: ")
    
    # Assess the strength of the password
    feedback = assess_password_strength(password)
    
    # Print the feedback
    print("\nPassword Strength Assessment:")
    for line in feedback:
        print(f"- {line}")

if __name__ == "__main__":
    main()
