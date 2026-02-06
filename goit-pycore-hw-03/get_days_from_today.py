from datetime import datetime

def get_days_from_today(date):
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        difference_in_days = current_date - formatted_date
    except ValueError:
        return "Error: incorrect date format. Please use YYYY-MM-DD format"

    return difference_in_days.days

correct_date = get_days_from_today('2026-02-01')
incorrect_date = get_days_from_today('2026.02.01')

print(correct_date)
print(incorrect_date)