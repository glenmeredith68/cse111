from datetime import datetime

now = datetime.now()
print(now)
day_of_week = now.weekday()
print(day_of_week)
weekday_names = ['Monday', "Tuesday", 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(f'Today is {weekday_names[day_of_week]}. ')
