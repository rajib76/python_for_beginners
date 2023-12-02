import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Create a specific date
specific_date = datetime.datetime(2023, 4, 15)

# Calculate the difference between two dates
date_difference = specific_date - current_datetime

# Format a date as a string
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print("Current Date and Time:", current_datetime)
print("Specific Date:", specific_date)
print("Date Difference:", date_difference)
print("Formatted Date:", formatted_date)
