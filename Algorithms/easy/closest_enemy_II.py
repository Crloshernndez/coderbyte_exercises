"""
Closest Enemy II
Have the function ClosestEnemyII(strArr) read the matrix of numbers stored in strArr which will be a 2D matrix that
contains only the integers 1, 0, or 2. Then from the position in the matrix where a 1 is, return the number of spaces
either left, right, down, or up you must move to reach an enemy which is represented by a 2. You are able to wrap
around one side of the matrix to the other as well. For example: if strArr is ["0000", "1000", "0002", "0002"] then
this looks like the following:

0 0 0 0
1 0 0 0
0 0 0 2
0 0 0 2

For this input your program should return 2 because the closest enemy (2) is 2 spaces away from the 1 by moving left
to wrap to the other side and then moving down once. The array will contain any number of 0's and 2's, but only a
single 1. It may not contain any 2's at all as well, where in that case your program should return a 0.

Examples
  Input: ["000", "100", "200"]
  Output: 1

  Input: ["0000", "2010", "0000", "2002"]
  Output: 2
"""

def ClosestEnemyII(strArr):
  steps = []

  grid = [[x for x in z] for z in strArr]
  large_grid = len(grid[0])

  pos_1 = None
  enemy_pos = [];
  for index, row in enumerate(grid):
    for i, elem in enumerate(row):
      if elem == "1":
        pos_1 = [index, i]
        continue
      if elem == "2":
        enemy_pos.append([index ,i])

  if len(enemy_pos) == 0: return 0

  for i, elem in enumerate(enemy_pos):
    res = [abs(x - y) for x, y in zip(pos_1, elem)]
    
    if res[1] > large_grid // 2:
      res[1] = abs(elem[1] - large_grid) + pos_1[1]
    
    if res[0] > large_grid // 2:
      res[0] = abs(elem[0] - large_grid) + pos_1[0]
    steps.append(sum(res))

  return min(steps)

# keep this function call here 
print(ClosestEnemyII(input()))

"""
Tests

1. For input ["10", "02"] the output was incorrect. The correct output is 2

2. For input ["01000", "00020", "00000", "00002", "02002"] the output was incorrect. The correct output is 1

3. For input ["01200", "00020", "00000", "00002", "02002"] the output was incorrect. The correct output is 1

4. For input ["01000", "00000", "00000", "00000", "00000"] the output was incorrect. The correct output is 0

5. For input ["00000", "10020", "00000", "00002", "02002"] the output was incorrect. The correct output is 2

6. For input ["00000", "10000", "00000", "00002", "02002"] the output was incorrect. The correct output is 3

7. For input ["0000000", "0001000", "0000000", "0000000", "0000000", "2000000", "0000000"] the output was incorrect. The correct output is 6

"""