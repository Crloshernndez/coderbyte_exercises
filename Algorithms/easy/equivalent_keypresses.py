"""
Equivalent Keypresses
Have the function EquivalentKeypresses(strArr) read the array of strings stored in strArr 
which will contain 2 strings representing two comma separated lists of keypresses. 
Your goal is to return the string true if the keypresses produce the same printable 
string and the string false if they do not. A keypress can be either a printable 
character or a backspace represented by -B. You can produce a printable string from 
such a string of keypresses by having backspaces erase one preceding character.

Examples
  Input: ["a,b,c,d", "a,b,c,d,-B,d"]
  Output: true

  Input: ["c,a,r,d", "c,a,-B,r,d"]
  Output: false
"""

def keyPress(string):
  test = []
  for index in string:
    if index == "-B":
      if len(test) > 0:
        test.pop()
    else:
      test.append(index)
    print(test)
  
  if len(test) < 1:
    test.append('')
  return test


def EquivalentKeypresses(strArr):
  a, b = strArr[0].split(','), strArr[1].split(',')

  str1 = keyPress(a)
  str2 = keyPress(b)

  if len(str1) > len(str2):
    return False
  
  is_equivalent = False

  count = 0
  for elem in str2:
    if count < len(str1):
      if is_equivalent == False:
        if elem == str1[0]:
            is_equivalent = True
            count += 1
      else:
        if elem == str1[count]:
          count += 1
        else:
          return False
    else:
      return is_equivalent
  return is_equivalent

# keep this function call here 
print(EquivalentKeypresses(["a,b,c,d", "a,b,c,d,d,-B"]))