#30 Days of Python (Date, time)

import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

from datetime import datetime, time
now = datetime.now()
print(now)                      
d = now.day                   
m = now.month               
y = now.year                 
h = now.hour                 
m = now.minute             
s = now.second
timestamp = now.timestamp()
print(d, m, y, h, m, timestamp)

formated = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formated)

today = "5 December, 2019"
today_date = datetime.strptime(today, "%d %B, %Y")
print(today_date)

from datetime import datetime
today = datetime(2020, 8, 25)
new_year = datetime(2020, 1, 1)
print(new_year)      
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) 
print(f'{day}/{month}/{year}, {hour}:{minute}')  
time_diff = new_year - today
print(time_diff)

new_time = datetime(1970, 1, 1)
print(today-new_time)
