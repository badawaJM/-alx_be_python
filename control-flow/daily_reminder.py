task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!.")
        else:
            print(f"Reminder: {task} is a high priority task that should be completed today, but it is not time-bound.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that should be completed today.")
        else:
            print(f"Reminder: {task} is a medium priority task that can be completed today or later.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task that should be completed today, but it is not urgent.")
        else:
            print(f"Reminder: {task} is a low priority task that can be done at your convenience.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
