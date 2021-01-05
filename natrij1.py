from datetime import datetime 
from datetime import timedelta
import sys

s1 = input()
s2 = input()

if s1 == s2:
    print('24:00:00')
    sys.exit()

FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
if tdelta.days < 0:
    tdelta = timedelta(days=0,
                seconds=tdelta.seconds, microseconds=tdelta.microseconds)

result = str(tdelta)

if len(result) == 7:
    print('0'+result)
elif len(result)>7:
    print(tdelta)
else:
    print('00:00:00')
 
 
