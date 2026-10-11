<<<<<<< HEAD
# 🔐 Random Password Generator
=======
# 💰 Expense Tracker
>>>>>>> 27a77bce1c6676fb24bd53eb714e594804eee0ca

## Author
Warda - Python Development Intern at DecodeLabs

## Description
<<<<<<< HEAD
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
=======
A Python script that takes continuous expense entries from the user,
accumulates them using an accumulator pattern, and displays the total spent.

## Features
- Continuous expense entry until user types 'done'
- Running total displayed after each entry
- Input validation (negative numbers & invalid input handled)
- Final summary: total, count, average, and breakdown

## Key Concept: Accumulator
```python
total = 0.0
total = total + expense   # Core pattern
>>>>>>> 27a77bce1c6676fb24bd53eb714e594804eee0ca
