"""
Arith Geo
Have the function ArithGeo(arr) take the array of numbers stored in arr and return the string "Arithmetic"
if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern.
If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference
between each of the numbers is consistent, where as in a geometric sequence, each term after the first
is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric
example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be entered,
and no array will contain all the same elements.

Examples
  Input: [5,10,15]
  Output: Arithmetic

  Input: [2,4,16,24]
  Output: -1
"""

def ArithGeo(arr):
  d = arr[1] - arr[0]
  r = arr[1] / arr[0]
  if all(arr[n+1] - arr[n] == d for n in range(len(arr)-1)):
     return 'Arithmetic'
  
  if all(arr[n+1] / arr[n] == r for n in range(len(arr)-1)):
    return 'Geometric'
  
  return -1

# keep this function call here 
print(ArithGeo(input()))