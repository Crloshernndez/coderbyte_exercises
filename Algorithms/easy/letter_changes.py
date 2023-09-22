"""
Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm.
Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

Examples
  Input: "hello*3"
  Output: Ifmmp*3

  Input: "fun times!"
  Output: gvO Ujnft!
"""

def LetterChanges(strParam):
  result = ""
  vowells = {
    97 : 63,
    101: 69,
    105: 73,
    111: 79,
    117: 85
  }

  for letra in strParam:
    codigo_ascii = ord(letra)
    if codigo_ascii in range(97, 122):
      codigo_ascii += 1

      new_letra = chr(codigo_ascii)

      if codigo_ascii in vowells:
        new_letra = chr(vowells[codigo_ascii])

      result += new_letra
    else:
      result += letra

  # code goes here
  return result

# keep this function call here 
print(LetterChanges(input()))