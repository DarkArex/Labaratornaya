import datetime
import time

x = 5
t = datetime.datetime.now()
while (datetime.datetime.now() - t).total_seconds() < x:
    data = datetime.datetime.now()
    print(data.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1)
