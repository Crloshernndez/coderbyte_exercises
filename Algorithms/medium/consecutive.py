"""
Consecutive
Have the function Consecutive(arr) take the array of integers stored in arr and return the minimum
number of integers needed to make the contents of arr consecutive from the lowest number to the
highest number.
For example: If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be
added to the array (5 and 7) to make it a consecutive array of numbers from 4 to 8. Negative
numbers may be entered as parameters and no array will have less than 2 elements.

Examples
  Input: [5,10,15]
  Output: 8

  Input: [-2,10,4]
  Output: 10

"""

import unittest


def Consecutive(arr):
    arr.sort()

    counter = 0
    for i in range(arr[0], arr[-1] + 1):
        if i not in arr:
            counter += 1
    return counter


# keep this function call here
print(Consecutive([-2, 10, 4]))

# TESTS


class TestConsecutive(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(Consecutive([1, 2, 3, 4]), 0)

    def test_case_2(self):
        self.assertEqual(Consecutive([2, 5]), 2)

    def test_case_3(self):
        self.assertEqual(Consecutive([0, 3]), 2)

    def test_case_4(self):
        self.assertEqual(Consecutive([1, 23, 5]), 20)

    def test_case_5(self):
        self.assertEqual(Consecutive([100, 105, 110]), 8)

    def test_case_6(self):
        self.assertEqual(Consecutive([-4, -3, 5]), 7)

    def test_case_7(self):
        self.assertEqual(Consecutive([5, 12, 15, 17, 18, 22]), 12)

    def test_case_8(self):
        self.assertEqual(Consecutive([2, 3]), 0)

    def test_case_9(self):
        self.assertEqual(Consecutive([-4, 10]), 13)

    def test_case_10(self):
        self.assertEqual(Consecutive([1, 5, 9, 10, 11, 12, 14]), 7)


if __name__ == '__main__':
    unittest.main()
