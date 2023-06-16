"""
Rectangle Area

Have the function RectangleArea(strArr) take the array of strings stored in strArr, which will only contain 4 elements
and be in the form (x y) where x and y are both integers, and return the area of the rectangle formed by the 4 points
on a Cartesian grid. The 4 elements will be in arbitrary order. For example:
if strArr is ["(0 0)", "(3 0)", "(0 2)", "(3 2)"] then your program should return 6 because the width of the rectangle
is 3 and the height is 2 and the area of a rectangle is equal to the width * height

Examples
  Input: ["(1 1)","(1 3)","(3 1)","(3 3)"]
  Output: 4

  Input: ["(0 0)","(1 0)","(1 1)","(0 1)"]
  Output: 1
"""

import re

def RectangleArea(strArr):
  arr = [re.findall(r'\d+',s) for s in strArr]

  x = [int(s[0]) for s in arr]
  y = [int(s[1]) for s in arr]

  area = (max(x) - min(x))*(max(y) - min(y))
  return area

# keep this function call here 
print(RectangleArea(input()))