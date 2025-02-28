#1
import datetime

current_date = datetime.date.today()
print(f"Current date today is: {current_date}")
current_date = datetime.date.today() - datetime.timedelta(days=5)

print(f"After substract five days: {current_date}")

#2
import datetime

current_date = datetime.date.today()

yesterday = datetime.date.today() - datetime.timedelta(days=1)
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
print(f"Yesterday was {yesterday.strftime('%A')}. Today is {current_date.strftime('%A')}. Tomorrow will be {tomorrow.strftime('%A')}.") 

#3
import datetime

current_datetime = datetime.datetime.now()

datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Original datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)

#4
import datetime
date1 = input("Enter the first date in format(DATE-MONTH-YEAR)(Example: 4-6-2003):")
date1 = datetime.datetime.strptime(date1, "%d-%m-%Y")

date2 = input("Enter the second date in format(DATE-MONTH-YEAR)(Example: 4-6-2003):")
date2 = datetime.datetime.strptime(date2, "%d-%m-%Y")

delta = date1 - date2

delta = abs(delta.total_seconds())

print(f"The difference between two dates in seconds is: {delta}")