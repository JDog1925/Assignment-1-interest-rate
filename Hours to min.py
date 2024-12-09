# Input display time in hours
time_in_hours = float(input("Enter time duration in hours: "))

# Conversion factors
Minutes_per_hour = 60
Seconds_per_minutes = 60

# Conversion factor from hours to minutes and seconds
total_minutes = time_in_hours * Minutes_per_hour
minutes = int(total_minutes)
seconds = (total_minutes - minutes) * Seconds_per_minutes

print(f"Time duration: {minutes} minutes and {seconds:.2f} seconds")

