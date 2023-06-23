"""
Time Difference
Have the function TimeDifference(strArr) read the array of strings stored in strArr which will be an unsorted list
of times in a twelve-hour format like so: HH:MM(am/pm). Your goal is to determine the smallest difference in minutes
between two of the times in the list. For example: if strArr is ["2:10pm", "1:30pm", "10:30am", "4:42pm"] then your
program should return 40 because the smallest difference is between 1:30pm and 2:10pm with a difference of 40 minutes.
The input array will always contain at least two elements and all of the elements will be in the correct format and
unique.

Examples
  Input: ["1:10pm", "4:40am", "5:00pm"]
  Output: 230

  Input: ["10:00am", "11:45pm", "5:00am", "12:01am"]
  Output: 16
"""

import itertools
from datetime import datetime, timedelta

def TimeDifference(strArr):
  convinations = itertools.combinations(sorted(strArr), 2)

  lower = 0
  for t in convinations:
    a = datetime.strptime(t[0], '%I:%M%p')
    b = datetime.strptime(t[1], '%I:%M%p')

    diff = timedelta(hours=a.hour - b.hour, minutes=a.minute - b.minute)
    minutos_diff = 1440 - int(diff.seconds / 60)
    
    lower = minutos_diff if minutos_diff < lower or lower == 0 else lower

  # code goes here
  return lower

# keep this function call here 
print(TimeDifference(input()))