import calendar

def count_days(year, month, whichday):
    # Generate the calendar for the month
    cal = calendar.monthcalendar(year, month)
    day_count = 0

    # Count occurances of the specific day of the week
    for week in cal:
        if week[whichday] != 0: # The day of the week is in this week
            day_count += 1

    return day_count

print(count_days(2025, 12, 0))
#expected result: 5