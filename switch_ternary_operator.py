day_messages = {
    "monday": "Today is Monday.",
    "tuesday": "Today is Tuesday.",
    "wednesday": "Today is Wednesday.",
    "thursday": "Today is Thursday.",
    "friday": "Today is Friday.",
    "saturday": "Today is Saturday.",
    "sunday": "Today is Sunday."
}

day = input("Enter a day of the week: ").strip().lower()
message = day_messages.get(day, "Invalid day entered.")

if day in ("saturday", "sunday"):
    day_type = "Weekend"
elif day in ("monday", "tuesday", "wednesday", "thursday", "friday"):
    day_type = "Weekday"
else:
    day_type = "Unknown"  # Handles invalid input

print(message)
if day_type != "Unknown":
    print("It's a", day_type + ".")