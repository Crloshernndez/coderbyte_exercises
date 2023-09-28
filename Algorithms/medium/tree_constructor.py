"""
Tree Constructor
Have the function TreeConstructor(strArr) take the array of strings stored in strArr, which will contain pairs of
integers in the following format: (i1,i2), where i1 represents a child node in a tree and the second integer i2
signifies that it is the parent of i1. For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the
following tree:

      4
    /
   2
  / \
1    7

which you can see forms a proper binary tree. Your program should, in this case, return the string true because a
valid binary tree can be formed. If a proper binary tree cannot be formed with the integer pairs, then return the
string false. All of the integers within the tree will be unique, which means there can only be one node in the tree
with the given integer value.

Examples
  Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
  Output: true
  
  Input: ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
  Output: false
"""

import unittest


def treeConstructor(strArr):
    parent_list = []
    child_list = []

    for node in strArr:
        child, parent = eval(node)
        parent_list.append(parent)

        if parent_list.count(parent) > 2:
            return "False"

        if child not in child_list:
            child_list.append(child)
        else:
            return "False"

    return "True"


# keep this function call here
# print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]))

# Tests
class TestTreeConstructor(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(treeConstructor(["(1,2)", "(2,4)", "(7,2)"]), "True")

    def test_case_2(self):
        self.assertEqual(treeConstructor(
            ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]), "True")

    def test_case_3(self):
        self.assertEqual(treeConstructor(
            ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]), "False")

    def test_case_4(self):
        self.assertEqual(treeConstructor(["(2,5)", "(2,6)"]), "False")

    def test_case_5(self):
        self.assertEqual(treeConstructor(["(10,20)"]), "True")

    def test_case_6(self):
        self.assertEqual(treeConstructor(
            ["(2,3)", "(1,2)", "(4,9)", "(9,3)", "(12,9)", "(6,4)"]), "True")

    def test_case_7(self):
        self.assertEqual(treeConstructor(
            ["(2,3)", "(1,2)", "(4,9)", "(9,3)", "(12,9)", "(6,4)", "(1,9)"]), "False")

    def test_case_8(self):
        self.assertEqual(treeConstructor(["(1,2)", "(2,4)", "(7,4)"]), "True")

    def test_case_9(self):
        self.assertEqual(treeConstructor(
            ["(5,6)", "(6,3)", "(2,3)", "(12,5)"]), "True")

    def test_case_10(self):
        self.assertEqual(treeConstructor(["(10,20)", "(20,50)"]), "True")


if __name__ == "__main__":
    unittest.main()
