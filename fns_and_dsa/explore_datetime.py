from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, number_of_days):
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

# --- Main Program ---
if __name__ == "__main__":
    # Part 1: Display the current date and time
    current = display_current_datetime()

    # Part 2: Calculate the future date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current, days_to_add)
    except ValueError:
        print("Please enter a valid integer number of days.")
