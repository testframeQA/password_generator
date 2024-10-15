import argparse
import secrets
import string

def generate_token(length) -> str:
    token = secrets.token_hex(length)
    print(f"Secure {length}-alphanumeric token: {token}")
    return token

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a secure token.')
    parser.add_argument('length', type=int, help='Length of the token.')

    args = parser.parse_args()
    generate_token(args.length)
