# 🔐 Random Password Generator

## Author
Warda - Python Development Intern at DecodeLabs

## Description
A cryptographically secure random password generator that creates
strong passwords based on user-specified length using letters,
digits, and symbols.

## Features
- User-defined password length (8-128 characters)
- Cryptographically secure randomness (secrets module)
- Uses Python's string module for character classification
- Calculates entropy in bits (E = L × log₂(R))
- Evaluates password strength
- NIST 2024 compliance check

## Key Concepts
- Importing modules (`secrets`, `string`, `math`)
- String manipulation
- List comprehension + `.join()` for O(N) efficiency
- Cryptographic security vs pseudo-randomness
- Input validation

## How to Run
```bash
python password_generator.py