from datetime import datetime
import get_birthdays

users = [
        {'name': 'Jhonny', 'birthday': datetime(1985, 6, 21)},
        {'name': 'Michael', 'birthday': datetime(1981, 6, 24)},
        {'name': 'Robert', 'birthday': datetime(1991, 6, 25)},
        {'name': 'Kenneth', 'birthday': datetime(1984, 6, 26)},
        {'name': 'George', 'birthday': datetime(1979, 6, 27)},
        {'name': 'Ronald', 'birthday': datetime(1985, 6, 28)},
        {'name': 'Scott', 'birthday': datetime(2001, 6, 28)},
        {'name': 'Stephen', 'birthday': datetime(1995, 6, 29)},
        {'name': 'Anthony', 'birthday': datetime(1992, 6, 30)},
        {'name': 'Frank', 'birthday': datetime(1970, 7, 2)},
        {'name': 'Fernando', 'birthday': datetime(1979, 7, 4)},
        {'name': 'Arlene', 'birthday': datetime(1982, 7, 5)},
        {'name': 'Kristin', 'birthday': datetime(1983, 7, 5)},
        ]



get_birthdays.get_birthdays_per_week(users)