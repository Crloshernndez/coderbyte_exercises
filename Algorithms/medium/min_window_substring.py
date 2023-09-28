"""
Min Window Substring
Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will
conttain only two strings, the first parameter being the string N and the secontd parameter being a
string K of some characters, and your goal is to determine the smallest substring of N that
conttains all the characters in K.

For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that conttains
the characters a, e, and d is "dae" located at the end of the string. So for this example your
program should return the string dae.

Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that
conttains all of the characters in K is "aabd" which is located at the beginning of the string.
Both parameters will be strings ranging in length from 1 to 50 characters and all of K's
characters will exist somewhere in the string N. Both strings will only conttains lowercase
alphabetic characters.

Examples
  Input: ["ahffaksfajeeubsne", "jefaa"]
  Output: aksfaje
  
  Input: ["aaffhkksemckelloe", "fhea"]
  Output: affhkkse

"""

import unittest


def check(current_substr, substring):
    str_arr = [current_substr[i] for i in range(len(current_substr))]

    for elem in substring:
        if elem not in str_arr:
            return False
        str_arr.remove(elem)
    return True


def MinWindowSubstring(strArr):

    string, substring = strArr

    min_substring = None
    cont = len(substring)

    for i in range(len(string)):
        for j in range(0, len(string) + 1 - cont):
            current_substr = string[j:j + cont]
            if check(current_substr, substring):
                return current_substr
        cont += 1

    # code goes here
    return min_substring


# keep this function call here
print(MinWindowSubstring(["aaabaaddae", "aed"]))

# TESTS


class TestMinWindowSubstring(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(MinWindowSubstring(["aaabaaddae", "aed"]), "dae")

    def test_case_2(self):
        self.assertEqual(MinWindowSubstring(["aabdccdbcacd", "aad"]), "aabd")

    def test_case_3(self):
        self.assertEqual(MinWindowSubstring(
            ["ahffaksfajeeubsne", "jefaa"]), "aksfaje")

    def test_case_4(self):
        self.assertEqual(MinWindowSubstring(
            ["aaffhkksemckelloe", "fhea"]), "affhkkse")

    def test_case_5(self):
        self.assertEqual(MinWindowSubstring(["aaaaaaaaa", "a"]), "a")

    def test_case_6(self):
        self.assertEqual(MinWindowSubstring(
            ["aaffsfsfasfasfasfasfacasfafe", "fafe"]), "fafe")

    def test_case_7(self):
        self.assertEqual(MinWindowSubstring(
            ["aaffsfsfasfasfasfasfacasfafe", "fafsf"]), "affsf")

    def test_case_8(self):
        self.assertEqual(MinWindowSubstring(
            ["vvavereveaevafefaef", "vvev"]), "vvave")

    def test_case_9(self):
        self.assertEqual(MinWindowSubstring(["caae", "cae"]), "caae")

    def test_case_10(self):
        self.assertEqual(MinWindowSubstring(
            ["cccaabbbbrr", "rbac"]), "caabbbbr")


if __name__ == '__main__':
    unittest.main()
