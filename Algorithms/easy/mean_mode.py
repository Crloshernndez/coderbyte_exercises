"""
Mean Mode

Have the function MeanMode(arr) take the array of numbers stored in arr and return 1 if the mode equals the mean,
0 if they don't equal each other (ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)).
The array will not be empty, will only contain positive integers, and will not contain more than one mode.

Examples
  Input: [1, 2, 3]
  Output: 0

  Input: [4, 4, 4, 6, 2]
  Output: 1
"""

import collections

def MeanMode(arr):
  media = sum(arr) / len(arr)
  arr_set = set(arr)

  if len(arr_set) == len(arr):
    return 0

  contador = collections.Counter(arr)
  elemento_repetido = [elemento for elemento, count in contador.items() if count > 1][0]

  if elemento_repetido != media:
    return 0

  return 1

# keep this function call here 
print(MeanMode(input()))