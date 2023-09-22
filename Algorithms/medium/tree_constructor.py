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

1. For input ["(1,2)", "(2,4)", "(7,2)"] the output was incorrect. The correct output is true

2. For input ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"] the output was incorrect. The correct output is true

3. For input ["(1,2)", "(3,2)", "(2,12)", "(5,2)"] the output was incorrect. The correct output is false

4. For input ["(2,5)", "(2,6)"] the output was incorrect. The correct output is false

5. For input ["(10,20)"] the output was incorrect. The correct output is true

6. For input ["(2,3)", "(1,2)", "(4,9)", "(9,3)", "(12,9)", "(6,4)"] the output was incorrect. The correct output is true

7. For input ["(2,3)", "(1,2)", "(4,9)", "(9,3)", "(12,9)", "(6,4)", "(1,9)"] the output was incorrect. The correct output is false

8. For input ["(1,2)", "(2,4)", "(7,4)"] the output was incorrect. The correct output is true

9. For input ["(5,6)", "(6,3)", "(2,3)", "(12,5)"] the output was incorrect. The correct output is true

10. For input ["(10,20)", "(20,50)"] the output was incorrect. The correct output is true
"""


def TreeConstructor(strArr):
    parent_list = []
    child_list = []

    for node in strArr:
        child, parent = eval(node)
        parent_list.append(parent)

        if parent_list.count(parent) > 2:
            return False

        if child not in child_list:
            child_list.append(child)
        else:
            return False

    return "True"


# keep this function call here
print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]))
