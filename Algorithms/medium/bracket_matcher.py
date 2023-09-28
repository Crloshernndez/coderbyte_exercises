"""
Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the
brackets are correctly matched and each one is accounted for. Otherwise return 0.
For example: if str is "(hello (world))", then the output should be 1, but if str
is "((hello (world))" the the output should be 0 because the brackets do not correctly match up.
Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

EXAMPLE:
  Input: "(coder)(byte))"
  Output: 0
  
  Input: "(c(oder)) b(yte)"
  Output: 1
  
  Input: "the color re(d))()(()"
  Output: 0
"""
import unittest


def BracketMatcher(strParam):
    count = 0

    for i in strParam:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        else:
            continue

        if count < 0:
            return 0

    return 1 if count == 0 else 0


# keep this function call here
# print(BracketMatcher("the color re(d))()(()"))

# Tests
class TestBracketMatcher(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(BracketMatcher("hello()"), 1)

    def test_case_2(self):
        self.assertEqual(BracketMatcher("one(bracket)"), 1)

    def test_case_3(self):
        self.assertEqual(BracketMatcher("coder(b)(y)(t)(e))"), 0)

    def test_case_4(self):
        self.assertEqual(BracketMatcher("()coderbyte() yes()"), 1)

    def test_case_5(self):
        self.assertEqual(BracketMatcher("dogs and cats"), 1)

    def test_case_6(self):
        self.assertEqual(BracketMatcher("01()01()01()"), 1)

    def test_case_7(self):
        self.assertEqual(BracketMatcher("the color re(d))()(()"), 0)

    def test_case_8(self):
        self.assertEqual(BracketMatcher("letter(s) gal(o)(r)((e)"), 0)

    def test_case_9(self):
        self.assertEqual(BracketMatcher("three let(t)ers"), 1)

    def test_case_10(self):
        self.assertEqual(BracketMatcher("twice thri(c)(e)()()"), 1)


if __name__ == "__main__":
    unittest.main()
