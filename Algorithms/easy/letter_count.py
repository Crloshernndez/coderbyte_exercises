"""
Letter Count I

Have the function LetterCountI(str) take the str parameter being passed and return the first word with
the greatest number of repeated letters. For example: "Today, is the greatest day ever!" should return
greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there are
no words with repeating letters return -1. Words will be separated by spaces.

Examples
  Input: "Hello apple pie"
  Output: Hello

  Input: "No words"
  Output: -1
"""

def LetterCountI(strParam):
  arr = strParam.split(' ')

  valid = [word for word in arr if len(word) > len(set(word))]

  if len(valid) == 0:
    return -1
  
  return valid[0]

# keep this function call here 
print(LetterCountI(input()))