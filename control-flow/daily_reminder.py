# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case for priority handling (Python 3.10+)
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Task '{task}' has an unspecified priority"

# Check if the task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"

else:
    message += ". Consider completing it when you have free time."

# Output the final reminder
print()
print(message)
