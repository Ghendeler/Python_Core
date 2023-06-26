from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    birthdays_d = {}
    cur_datetime = datetime.now()
    cur_date = datetime(cur_datetime.year, cur_datetime.month, cur_datetime.day)
    cur_week_day = cur_date.isoweekday()
    date_start = cur_date + timedelta(days = 1)
    date_end = date_start + timedelta(days = 6)
    date_monday = cur_date + timedelta(days = 8 - cur_week_day)
    
    for user in users:
        birthday_cur = datetime(cur_date.year, user['birthday'].month, user['birthday'].day)
        if date_start <= birthday_cur <= date_end:
            if (birthday_cur.isoweekday() in [6, 7]) and (birthday_cur < date_monday): 
                birthday = date_monday
            elif birthday_cur.isoweekday() not in [6, 7]:
                birthday = birthday_cur
            else:
                continue
            if birthday in birthdays_d.keys():
                birthdays_d[birthday].append(user['name'])
            else:
                birthdays_d[birthday] = [user['name']]

    days = [k for k in birthdays_d.keys()]
    days.sort()
    for i in days:
        print(f'{i.date().strftime("%A")}: {", ".join(birthdays_d[i])}')
