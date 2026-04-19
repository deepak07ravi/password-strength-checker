import re

def password_checker():
    score = 0
    
    # Password input (VISIBLE)
    password = input("Enter your password: ")
    
    length = len(password)
    
    # Length scoring
    if length > 12:
        score += 3
    elif length > 8:
        score += 2
    elif length == 8:
        score += 1
    
    
    # Uppercase and lowercase check
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    
    if has_upper and has_lower:
        score += 2
    elif has_upper or has_lower:
        score += 1
    
    # Special character check
    special_chars = re.findall(r'[^a-zA-Z0-9]', password)
    
    if len(special_chars) == 1:
        score += 1
    elif len(special_chars) > 1:
        score += 2
    
    # Maximum score = 7
    max_score = 7
    percentage = (score / max_score) * 100
    
    # Strength label
    if percentage < 40:
        strength = "Weak"
    elif percentage < 75:
        strength = "Medium"
    else:
        strength = "Strong"
    
    # Final Output
    print("\nEntered password is:", password)
    print("Score is:", f"{score}/{max_score}")
    print("Strength %:", round(percentage, 2))
    print("Password Strength:", strength)
    
# Run function
password_checker()