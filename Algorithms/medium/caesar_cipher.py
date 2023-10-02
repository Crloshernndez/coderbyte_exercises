"""
Caesar Cipher
Have the function CaesarCipher(str,num) take the str parameter and perform a Caesar Cipher shift on it using the num
parameter as the shifting number. A Caesar Cipher works by shifting each letter in the string N places in
the alphabet (in this case N will be num). Punctuation, spaces, and capitalization should remain intact.
For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".

Examples
  Input: "Hello" & num = 4
  Output: Lipps

  Input: "abc" & num = 0
  Output: abc
"""

import unittest


def CaesarCipher(strParam, num):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    res = ''

    for i in range(len(strParam)):

        if not strParam[i].isalpha():
            res += strParam[i]
            continue

        indice = alp.index(strParam[i].lower())
        new_index = (indice + num) % 26

        new_char = alp[new_index]

        res += new_char if strParam[i].islower() else new_char.upper()

    # code goes here
    return res


# keep this function call here
# print(CaesarCipher("dogs", 8))  # lwoa

# TESTS


class TestCaesarCipher(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(CaesarCipher("Hello", 4), "Lipps")

    def test_case_2(self):
        self.assertEqual(CaesarCipher("world!", 1), "xpsme!")

    def test_case_3(self):
        self.assertEqual(CaesarCipher("coderBYTE", 2), "eqfgtDAVG")

    def test_case_4(self):
        self.assertEqual(CaesarCipher("some change", 1), "tpnf dibohf")

    def test_case_5(self):
        self.assertEqual(CaesarCipher("what", 2), "yjcv")

    def test_case_6(self):
        self.assertEqual(CaesarCipher("dogs", 8), "lwoa")

    def test_case_7(self):
        self.assertEqual(CaesarCipher("byte", 13), "olgr")

    def test_case_8(self):
        self.assertEqual(CaesarCipher("aPPlication", 2), "cRRnkecvkqp")


if __name__ == "__main__":
    unittest.main()
