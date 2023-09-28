"""
Triple Double
Have the function TripleDouble(num1,num2) take both parameters being passed, and return 1 if there
is a straight triple of a number at any place in num1 and also a straight double of the same
number in num2.
For example: if num1 equals 451999277 and num2 equals 41177722899, then return 1 because in the
first parameter you have the straight triple 999 and you have a straight double, 99, of the same
number in the second parameter. If this isn't the case, return 0.

Examples
  Input: 465555 & num2 = 5579
  Output: 1

  Input: 67844 & num2 = 66237
  Output: 0
"""

import unittest


def TripleDouble(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)

    for i in range(len(num1_str) - 2):
        if num1_str[i] == num1_str[i + 1] == num1_str[i + 2]:
            triple = num1_str[i]
            if triple * 2 in num2_str:
                return 1

    return 0


# keep this function call here
# print(TripleDouble('451999277', '41177722899'))

# TEST
class TestTripleDouble(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(TripleDouble('1234', '1234'), 0)

    def test_case_2(self):
        self.assertEqual(TripleDouble('333', '33'), 1)

    def test_case_3(self):
        self.assertEqual(TripleDouble('12334455', '12355555'), 0)

    def test_case_4(self):
        self.assertEqual(TripleDouble('555666', '5589'), 1)

    def test_case_5(self):
        self.assertEqual(TripleDouble('5', '5'), 0)

    def test_case_6(self):
        self.assertEqual(TripleDouble('556668', '556886'), 0)

    def test_case_7(self):
        self.assertEqual(TripleDouble('3776777', '87766'), 1)

    def test_case_8(self):
        self.assertEqual(TripleDouble('17555', '55144'), 1)

    def test_case_9(self):
        self.assertEqual(TripleDouble('800000006', '7800'), 1)

    def test_case_10(self):
        self.assertEqual(TripleDouble('2233334', '3'), 0)


if __name__ == '__main__':
    unittest.main()
