"""
Find Intersection
Have the function FindIntersection(strArr) read the array of strings stored in strArr
which will contain 2 elements: 
the first element will represent a list of comma-separated numbers sorted in ascending order, 
the second element will represent a second list of comma-separated numbers (also sorted). 

Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. 
If there is no intersection, return the string false.

Examples
  Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
  Output: 1,4,13

  Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
  Output: 1,9,10
"""

def FindIntersection(strArr):
  str1, str2 = strArr[0], strArr[1]
  strArr = set(str1.split(', ')).intersection(str2.split(', '))
  strArr = sorted([int(num) for num in list(strArr)])
  strArr = [str(num) for num in strArr]

  if len(strArr) < 1:
      return False
  
  strArr = (', ').join(strArr)

  return strArr

# keep this function call here 
print(FindIntersection(input()))