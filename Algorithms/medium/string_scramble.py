"""
String Scramble
Have the function StringScramble(str1,str2) take both parameters being passed and return the
string true if a portion of str1 characters can be rearranged to match str2, otherwise return the
string false.
For example: if str1 is "rkqodlw" and str2 is "world" the output should return true. Punctuation
and symbols will not be entered with the parameters.

Examples
  Input: "cdore" & str2 = "coder"
  Output: true

  Input: "h3llko" & str2 = "hello"
  Output: false


"""

import unittest


def StringScramble(str1, str2):

    char_count_str1 = {}
    char_count_str2 = {}

    for char in str1:
        char_count_str1[char] = char_count_str1.get(char, 0) + 1

    for char in str2:
        char_count_str2[char] = char_count_str2.get(char, 0) + 1

    for char, count in char_count_str2.items():
        if char not in char_count_str1 or char_count_str1[char] < count:
            return False

    return True


# keep this function call here
# print(StringScramble('cdore', 'coder'))

# Tests


class TestStringScramble(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(StringScramble("coodrebtqqkye", "coderbyte"), True)

    def test_case_2(self):
        self.assertEqual(StringScramble("codrebtaqqq", "coderbyte"), False)

    def test_case_3(self):
        self.assertEqual(StringScramble("heloooolwrdlla", "helloworld"), True)

    def test_case_4(self):
        self.assertEqual(StringScramble("win33er", "winner"), False)

    def test_case_5(self):
        self.assertEqual(StringScramble("abcgggdfe", "abcdef"), True)

    def test_case_6(self):
        self.assertEqual(StringScramble("coamamaaqq", "comma"), True)

    def test_case_7(self):
        self.assertEqual(StringScramble("thsisifasl3", "thisisfalse"), False)

    def test_case_8(self):
        self.assertEqual(StringScramble("lettrrkakaeaaaqq", "letter"), True)

    def test_case_9(self):
        self.assertEqual(StringScramble("aqwe", "qa"), True)

    def test_case_10(self):
        self.assertEqual(StringScramble("yelowrqwedlk", "yellowred"), True)


if __name__ == '__main__':
    unittest.main()
