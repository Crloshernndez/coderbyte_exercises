"""
Dash Insert

Have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str.
For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number.

Examples
  Input: 99946
  Output: 9-9-946

  Input: 56730
  Output: 567-30
"""

def DashInsert(strParam):

  s = strParam[0]

  for i in range(1, len(strParam)):
    if int(strParam[i]) % 2 != 0 and int(strParam[i - 1]) % 2 != 0:
      s += '-'

    s += str(strParam)[i]
  # code goes here
  return s
print(DashInsert(input()))