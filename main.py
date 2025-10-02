expenses = {}

while True:
    entry = input("Enter expense (e.g. Food:200) or type 'summary' to view total: ").strip()

    if entry.lower() == 'summary':
        print("\nExpense Summary:")
        total = 0
        for category, amount in expenses.items():
            print(f"{category}: ₹{amount}")
            total += amount
        print(f"Total: ₹{total}\n")
        break
    else:
        try:
            category, amount = entry.split(":")
            amount = float(amount)
            expenses[category] = expenses.get(category, 0) + amount
        except:
            print("Invalid format. Use Category:Amount (e.g. Travel:150)")