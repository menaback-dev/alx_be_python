task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

while priority not in ("high", "medium", "low"):
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

reminder = f"'{task}' is a {priority} priority task"

match priority:
    case "high":
        reminder += ""
    case "medium":
        reminder += ""
    case "low":
        reminder += ""

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."

print("\nReminder:", reminder)