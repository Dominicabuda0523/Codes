# Write code below 💖
# main.py

import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2026, 4, 1)
days_away = next_birthday - today

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f'Your birthday is {days_away.days} days away!')

    