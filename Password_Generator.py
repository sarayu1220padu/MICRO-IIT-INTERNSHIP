import random
import secrets
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    # Define character sets based on user preferences
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Ensure at least one character type is selected
    if not characters:
        print("Error: You must select at least one character type.")
        return None
    
    # Generate the password using a secure random generator
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    # Get password length
    while True:
        try:
            length = int(input("Enter the password length: "))
            if length > 0:
                break
            else:
                print("Password length must be greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # Get character preferences
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    return length, use_uppercase, use_lowercase, use_numbers, use_special

def main():
    print("Welcome to the Password Generator!")
    print("This tool will help you create a strong and secure password.")
    
    while True:
        # Get user preferences
        length, use_uppercase, use_lowercase, use_numbers, use_special = get_user_preferences()
        
        # Generate the password
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        
        if password:
            print(f"\nYour generated password is: {password}")
        
        # Ask if the user wants to generate another password
        another = input("\nDo you want to generate another password? (yes/no): ").lower()
        if another != 'yes':
            print("Thank you for using the Password Generator. Have a nice day!")
            break

# Run the program
if __name__ == "__main__":
    main()