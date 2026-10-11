"""
Project: Expense Tracker
Author: Warda
Domain: Python Development - DecodeLabs Internship
Description: A script that takes continuous expense entries from the user,
             accumulates them, and displays the total spent.
Key Skill: Math operations & Accumulators (total = total + new_expense)
"""

def main():
    print("=" * 45)
    print("       💰 EXPENSE TRACKER 💰")
    print("=" * 45)
    print("Enter your expenses one by one.")
    print("Type 'done' when finished to see the total.\n")

    total = 0.0          # 🔑 Accumulator variable
    count = 0            # Number of expenses entered
    expenses = []        # Optional: store all expenses for summary

    while True:
        user_input = input("Enter expense amount (or 'done' to finish): ").strip()

        # Exit condition
        if user_input.lower() == "done":
            break

        # Validate input
        try:
            expense = float(user_input)

            if expense < 0:
                print("❌ Expense cannot be negative. Try again.\n")
                continue

            # 🔑 Accumulate the total
            total = total + expense       # Core concept!
            count += 1
            expenses.append(expense)

            print(f"✅ Added: {expense:.2f}  |  Running Total: {total:.2f}\n")

        except ValueError:
            print("❌ Invalid input! Please enter a number or 'done'.\n")

    # Final summary
    print("\n" + "=" * 45)
    print("           📊 FINAL SUMMARY")
    print("=" * 45)

    if count == 0:
        print("No expenses were entered.")
    else:
        print(f"Number of Expenses : {count}")
        print(f"Total Spent        : {total:.2f}")
        print(f"Average Expense    : {total / count:.2f}")

        # Show breakdown (optional)
        print("\nExpense Breakdown:")
        for i, exp in enumerate(expenses, start=1):
            print(f"  {i}. {exp:.2f}")

    print("=" * 45)
    print("👋 Thank you for using Expense Tracker!")


if __name__ == "__main__":
    main()