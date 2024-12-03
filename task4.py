from datetime import datetime, timedelta


def get_upcoming_birthdays(users: dict) -> dict:
    current_date = datetime.today().date()

    congratulation_list = []

    for user in users:
        birthday_obj = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        current_year_birthday = birthday_obj.replace(year=current_date.year)

        if current_year_birthday < current_date:
            current_year_birthday = current_year_birthday.replace(year=current_date.year + 1)

        days_to_birthday = (current_year_birthday - current_date).days

        if 0 <= days_to_birthday < 7:
            congr_date = current_year_birthday

            if current_year_birthday.weekday() >= 5:
                congr_date = current_date + timedelta(days=(7 - current_date.weekday()))

            congratulation_list.append(
                    {
                        "name": user["name"],
                        "congratulation_date": congr_date.strftime("%Y.%m.%d"),
                    }
                )

    return congratulation_list

users = [
    {"name": "Nick", "birthday": "1992.12.09"},
    {"name": "Emili", "birthday": "1987.08.10"},
    {"name": "Tom", "birthday": "2001.12.07"},
    {"name": "Eva", "birthday": "2006.05.16"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
