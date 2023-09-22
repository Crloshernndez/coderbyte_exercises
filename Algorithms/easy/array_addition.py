"""
Array Addition I

Have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return the string true
if any combination of numbers in the array (excluding the largest number) can be added up to equal the largest
number in the array, otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3]
the output should return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all
the same elements, and may contain negative numbers.

Examples
  Input: [5,7,16,1,2]
  Output: false

  Input: [3,5,-1,8,12]
  Output: true
"""

import itertools

def ArrayAdditionI(arr):
  h = max(arr)
  arr.remove(h)

  convinations = []

  for i in range(2, len(arr) + 1):
    convinations.extend(itertools.combinations(arr, i))

  for elem in convinations:
    if sum(elem) == h:
      return True

  # code goes here add sum
  return False
print(ArrayAdditionI(input()))