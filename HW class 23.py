import random
import string


def generate_password(length):
    if length < 6:
        print("Password should be at least 6 characters long.")
        return

    
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digits = list(string.digits)

    
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    
    all_chars = lower + upper + digits
    remaining_length = length - len(password)
    password += random.choices(all_chars, k=remaining_length)

    
    random.shuffle(password)

    
    return ''.join(password)



length = 10 
password = generate_password(length)
print("Generated Password:", password)
