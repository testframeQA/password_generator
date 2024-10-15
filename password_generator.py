import argparse
import secrets
import string

def generate_password(length, digits) -> str:
    if digits > length:
        raise ValueError("Number of digits cannot exceed the total password length.")

    chosen_digits = ''.join(secrets.choice(string.digits) for _ in range(digits))
    chosen_letters = ''.join(secrets.choice(string.ascii_letters) for _ in range(length - digits))
    chosen_special_chars = ''.join(secrets.choice(string.punctuation) for _ in range(length - digits))

    password_list = list(chosen_digits + chosen_letters + chosen_special_chars)
    secrets.SystemRandom().shuffle(password_list)

    password = ''.join(password_list)

    print(f"{length}-character password with {digits} digits: {password}")

    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a random password.')
    parser.add_argument('length', type=int, help='Length of the password.')
    parser.add_argument('digits', type=int, help='Number of digits in the password.')
    args = parser.parse_args()
    generate_password(args.length, args.digits)
