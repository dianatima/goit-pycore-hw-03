from datetime import datetime;

def get_days_from_today(date):
    try:
        date_obj=datetime.strptime(date, "%Y-%m-%d")
        current_date=datetime.today()
        return (current_date-date_obj).days
    except ValueError:
        return "Invalid date format"
    
print(get_days_from_today("2024-12-24"))