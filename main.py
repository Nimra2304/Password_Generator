import secrets
import string

def generate_password(length: int) -> str:
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    return ''.join(secrets.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("Your Generated Password!!")
    
    try:
        user_length = int(input("Enter desired password length: "))
        if user_length < 1:
            print("Password length must be at least 1.")
        else:
            password = generate_password(user_length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid integer for the length.")