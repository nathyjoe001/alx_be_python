# daily_reminder.py

def daily_reminder():
    # Prompt for user input
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Process the task based on priority using Match Case
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level. Please choose high, medium, or low.")
            return

    # Add additional details if the task is time-bound
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    elif time_bound == "no":
        message += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time sensitivity. Please answer with yes or no.")
        return

    # Print the customized reminder
    print(f"Reminder: {message}")

if __name__ == "__main__":
    daily_reminder()
