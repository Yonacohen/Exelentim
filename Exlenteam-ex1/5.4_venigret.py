
import random
import datetime

date_str1 = input("Enter a date in YYYY-MM-DD format: ")
date_obj1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d")

date_str2 = input("Enter a second date in YYYY-MM-DD format: ")
date_obj2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d")

time_between_dates = date_obj2 - date_obj1
time_between_dates = time_between_dates.days

ranDay = random.randrange(time_between_dates)

ranDate = date_obj1 + datetime.timedelta(days=ranDay)

print (ranDate)
if (ranDate.weekday()==0):
    print ("I have not vinigret")















