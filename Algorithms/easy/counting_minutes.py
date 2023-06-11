"""
Counting Minutes I

Have the function CountingMinutesI(str) take the str parameter being passed which will be two times 
(each properly formatted with a colon and am or pm) separated by a hyphen and return the total number
of minutes between the two times. The time will be in a 12 hour clock format. For example: if str is
9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am the output should be 1320.

Examples
  Input: "12:30pm-12:00am"
  Output: 690

  Input: "1:23am-1:08am"
  Output: 1425
"""

from datetime import datetime, timedelta

def CountingMinutesI(strParam):
  hora1 = datetime.strptime(strParam.split('-')[0], '%I:%M%p')
  hora2 = datetime.strptime(strParam.split('-')[1], '%I:%M%p')
  
  if hora1 > hora2:
    diff = timedelta(hours=hora1.hour - hora2.hour, minutes=hora1.minute - hora2.minute)
    minutos_diff = 1440 - int(diff.seconds / 60)
    return minutos_diff
  else :
    diff = timedelta(hours=hora2.hour - hora1.hour, minutes=hora2.minute - hora1.minute)
    minutos_diff = int(diff.seconds / 60)
    return minutos_diff

# keep this function call here 
print(CountingMinutesI(input()))