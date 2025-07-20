task = input("Enter your task: ")
tasks_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match tasks_priority.lower():
    case "high":
        if time_bound.lower() == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!.")
        else:
            print(f"{task} is a high priority task that should be completed today, but it is not time-bound.")
    case "medium":
        if time_bound.lower() == "yes":
            print(f"{task} is a medium priority task that should be completed today.")
        else:
            print(f"{task} is a medium priority task that can be completed today or later.")
    case "low":
        if time_bound.lower() == "yes":
            print(f"{task} is a low priority task that should be completed today, but it is not urgent.")
        else:
            print(f"{task} is a low priority task that can be done at your convenience.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
