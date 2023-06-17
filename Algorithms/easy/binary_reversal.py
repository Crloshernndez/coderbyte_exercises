"""
Binary Reversal

Have the function BinaryReversal(str) take the str parameter being passed, which will be a positive integer,
take its binary representation (padded to the nearest N * 8 bits), reverse that string of bits, and then finally
return the new reversed string in decimal form. For example: if str is "47" then the binary version of this integer
is 101111 but we pad it to be 00101111. Your program should reverse this binary string which then becomes: 11110100
and then finally return the decimal version of this string, which is 244.

Examples
  Input: "213"
  Output: 171

  Input: "4567"
  Output: 60296
"""

def BinaryReversal(strParam):

  binario = bin(int(strParam))[2:]
  longitud_binario = len(binario)
  bytes_necesarios = -(-longitud_binario // 8)
  bits_deseados = 4 * 8

  if bits_deseados > longitud_binario:
    binario_rellenado = binario.zfill(bytes_necesarios * 8)[::-1]
  else:
    binario_rellenado = binario

  res = int(binario_rellenado, 2)

  # code goes here
  return res


# keep this function call here 
print(BinaryReversal(input()))