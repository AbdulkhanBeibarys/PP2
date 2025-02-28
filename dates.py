#1
import datetime
x = datetime.datetime
print(x.now())

#2
import datetime
x = datetime.datetime.now()
print(x.strftime('%A'))

#3
import datetime
x = datetime.datetime(2024, 8, 20)
print(x.strftime('%d'))
