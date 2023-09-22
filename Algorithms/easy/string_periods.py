"""
String Periods
Have the function StringPeriods(str) take the str parameter being passed and determine if there is some substring K
that can be repeated N > 1 times to produce the input string exactly as it appears. Your program should return the
longest substring K, and if there is none it should return the string -1.

For example: if str is "abcababcababcab" then your program should return abcab because that is the longest substring
that is repeated 3 times to create the final string. Another example: if str is "abababababab" then your program should
return ababab because it is the longest substring. If the input string contains only a single character, your program
should return the string -1.

Examples
  Input: "abcxabc"
  Output: -1

  Input: "affedaaffed"
  Output: -1

  Input: "gg"
  Output: g
"""

def StringPeriods(strParam):
  q = len(strParam)
  if q < 2: return -1

  div = [i for i in range(1, q + 1) if q % i == 0]

  res = -1
  for d in div:
      arr = [strParam[i:i+d] for i in range(0, q, d)][:-1]
      if len(arr) > 0 and len(set(arr)) == 1 and len(arr[0]) > res:
          res = len(arr.pop())
  # code goes here
  return strParam[:res] if res > 0 else res


# keep this function call here 
print(StringPeriods(input()))