"""
Project: Random Password Generator
Author: Warda
Domain: Python Development - DecodeLabs Internship
Description: Generates a cryptographically secure random password
             based on user-specified length using letters, digits, and symbols.
Key Skill: Importing Modules (secrets, string) & String Manipulation
"""

import string
import secrets
import math


def get_password_length():
    """
    Phase 1: Input — Get and validate password length from user.
    NIST 2024: Minimum 15 characters recommended for high security.
    """
    while True:
        try:
            length = int(input("Enter desired password length (min 8, recommended 15+): "))

            if length < 8:
                print(" Password must be at least 8 characters long. Try again.\n")
                continue

            if length > 128:
                print("Maximum length is 128 characters. Try again.\n")
                continue

            return length

        except ValueError:
            print(" Invalid input! Please enter a number.\n")


def build_character_pool():
    """
    Phase 2a: Build the character pool from Python's string module.
    Using string module instead of manual arrays (enterprise standard).
    """
    pool = string.ascii_letters + string.digits + string.punctuation
    return pool


def generate_password(length, pool):
    """
    Phase 2b: Build the backend transformation engine.

    Enterprise approach:
    - Use secrets.choice() for cryptographic security (NOT random.choice())
    - Use list + ''.join() for O(N) efficiency (NOT string += which is O(N^2))
    """
    password_chars = [secrets.choice(pool) for _ in range(length)]
    password = ''.join(password_chars)
    return password


def calculate_entropy(length, pool_size):
    """
    Phase 3: Mathematical provision of security.
    Entropy E = L x log2(R)
    L = password length
    R = character pool size
    """
    entropy = length * math.log2(pool_size)
    return entropy


def evaluate_strength(entropy_bits):
    """
    Evaluate password strength based on entropy bits.
    """
    if entropy_bits < 40:
        return "Weak"
    elif entropy_bits < 60:
        return "Moderate"
    elif entropy_bits < 80:
        return "Strong"
    else:
        return "Very Strong"


def main():
    """
    Main program — Input-Process-Output architecture.
    """
    print("=" * 50)
    print("       RANDOM PASSWORD GENERATOR")
    print("=" * 50)
    print("Generates cryptographically secure passwords.\n")

    length = get_password_length()
    pool = build_character_pool()
    password = generate_password(length, pool)

    entropy = calculate_entropy(length, len(pool))
    strength = evaluate_strength(entropy)

    print("\n" + "=" * 50)
    print("           YOUR PASSWORD")
    print("=" * 50)
    print(f"Password        : {password}")
    print(f"Length          : {length}")
    print(f"Character Pool  : {len(pool)} characters")
    print(f"Entropy         : {entropy:.2f} bits")
    print(f"Strength        : {strength}")
    print("=" * 50)

    if length < 15:
        print("\nNIST 2024 Tip: Use 15+ characters for high-security contexts.")
    else:
        print("\nMeets NIST 2024 minimum length requirement (15+).")

    print("\nGenerated using 'secrets' module (cryptographically secure).")
    print("Stay secure!")


if __name__ == "__main__":
    main()