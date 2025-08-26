import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for good strength.")
        return ""

    all_char = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(all_char) for _ in range(length))
    return password

def main():
    print(" Welcome to the Password Generator :")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            password = generate_password(length)
            if password:
                print(f"Generated Password: {password}\n")
        except ValueError:
            print("Please enter a valid number.")

        again = input("Do you want to generate another password? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye! Stay secure. ")
            break

main()
