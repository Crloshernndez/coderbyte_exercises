"""
Palindrome Swapper
Have the function PalindromeSwapper(str) take the str parameter being passed and determine if a palindrome can be
created by swapping two adjacent characters in the string. If it is possible to create a palindrome, then your program
should return the palindrome, if not then return the string -1. The input string will only contain alphabetic
characters. For example: if str is "rcaecar" then you can create a palindrome by swapping the second and third
characters, so your program should return the string racecar which is the final palindromic string.

Examples
  Input: "anna"
  Output: anna

  Input: "kyaak"
  Output: kayak
"""

def intercambiar_letras(cadena, pos1, pos2):
    lista_caracteres = list(cadena)
    lista_caracteres[pos1], lista_caracteres[pos2] = lista_caracteres[pos2], lista_caracteres[pos1]
    nueva_cadena = ''.join(lista_caracteres)
    return nueva_cadena

def PalindromeSwapper(strParam):
  for i in range(0, len(strParam) -1):
    res = intercambiar_letras(strParam, i, i+1)
    if res == res[::-1] : return res
  # code goes here
  return -1


# keep this function call here 
print(PalindromeSwapper(input()))