# 💰 Expense Tracker

## Author
Warda - Python Development Intern at DecodeLabs

## Description
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