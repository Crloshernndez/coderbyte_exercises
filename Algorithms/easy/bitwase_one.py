"""
Bitwise One

Have the function BitwiseOne(strArr) take the array of strings stored in strArr, which will only contain two strings
of equal length that represent binary numbers, and return a final binary string that performed the bitwise OR operation
on both strings. A bitwise OR operation places a 0 in the new string where there are zeroes in both binary strings,
otherwise it places a 1 in that spot. For example: if strArr is ["1001", "0100"] then your program should return
the string "1101"

Examples
  Input: ["100", "000"]
  Output: 100

  Input: ["00011", "01010"]
  Output: 01011
"""


def BitwiseOne(strArr):
  a, b= strArr
  res = ""

  for c1, c2 in zip(a, b):
    res += str(int(c1) | int(c2))


  # code goes here
  return res

# keep this function call here 
print(BitwiseOne(input()))