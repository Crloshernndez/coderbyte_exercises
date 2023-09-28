"""
Array Addition
Have the function ArrayAddition(arr) take the array of numbers stored in arr and return the string
true if any combination of numbers in the array (excluding the largest number) can be added up to
equal the largest number in the array, otherwise return the string false.
For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because
4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements,
and may contain negative numbers.

Examples
  Input: [5,7,16,1,2]
  Output: false

  Input: [3,5,-1,8,12]
  Output: true
"""

import unittest
import itertools


def ArrayAddition(arr):
    arr.sort()
    largest_number = arr.pop()

    for i in range(2, len(arr) + 1):
        combinations = list(itertools.combinations(arr, i))
        for combination in combinations:
            if sum(combination) == largest_number:
                return "True"

    # code goes here
    return "False"


# keep this function call here
# print(ArrayAddition([4, 6, 23, 10, 1, 3]))

# TESTS
class TestArrayAddition(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(ArrayAddition([1, 2, 3, 4]), "True")

    def test_case_2(self):
        self.assertEqual(ArrayAddition([2, 6, 18]), "False")

    def test_case_3(self):
        self.assertEqual(ArrayAddition([10, 20, 30, 40, 100]), "True")

    def test_case_4(self):
        self.assertEqual(ArrayAddition([10, 12, 500, 1, -5, 1, 0]), "False")

    def test_case_5(self):
        self.assertEqual(ArrayAddition([-2, -3, -4, -1, 100]), "False")

    def test_case_6(self):
        self.assertEqual(ArrayAddition([54, 49, 1, 0, 7, 4]), "True")

    def test_case_7(self):
        self.assertEqual(ArrayAddition([3, 4, 5, 7]), "True")

    def test_case_8(self):
        self.assertEqual(ArrayAddition([1, 1, 1, 1, 6]), "False")

    def test_case_9(self):
        self.assertEqual(ArrayAddition([2, 4, 6, 12, 92]), "False")

    def test_case_10(self):
        self.assertEqual(ArrayAddition([31, 2, 90, 50, 7]), "True")


if __name__ == "__main__":
    unittest.main()
