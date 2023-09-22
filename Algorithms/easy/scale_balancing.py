"""
Scale Balancing
Have the function ScaleBalancing(strArr) read strArr which will contain two elements, the first being the two positive
integer weights on a balance scale (left and right sides) and the second element being a list of available weights as
positive integers. Your goal is to determine if you can balance the scale by using the least amount of weights from
the list, but using at most only 2 weights. For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then this means there
is a balance scale with a weight of 5 on the left side and 9 on the right side. It is in fact possible to balance this
scale by adding a 6 to the left side from the list of weights and adding a 2 to the right side. Both scales will now
equal 11 and they are perfectly balanced. Your program should return a comma separated string of the weights that were
used from the list in ascending order, so for this example your program should return the string 2,6

There will only ever be one unique solution and the list of available weights will not be empty. It is also possible
to add two weights to only one side of the scale to balance it. If it is not possible to balance the scale then your
program should return the string not possible.

Examples
  Input: ["[3, 4]", "[1, 2, 7, 7]"]
  Output: 1

  Input: ["[13, 4]", "[1, 2, 3, 6, 14]"]
  Output: 3,6
"""

import itertools

def ScaleBalancing(strArr):

  balanza = eval(strArr[0])
  pesos = eval(strArr[1])

  pesos.insert(0,0)

  pesos_convinations = []

  for i in range(1, 3):
    pesos_convinations.extend(itertools.combinations(pesos, i))

  pesos_convinations = [list(i) for i in pesos_convinations]

  balanza_left = itertools.product([balanza[0]], pesos_convinations)
  balanza_rigth = itertools.product([balanza[1]], pesos_convinations)

  res = []
  for permutation in itertools.product(balanza_left, balanza_rigth):
    permutation = list(permutation)
    if sum([permutation[0][0],sum(permutation[0][1])]) == sum([permutation[1][0],sum(permutation[1][1])]):
      res.extend([*permutation[0][1],*permutation[1][1]])
      break

  if 0 in res: res.remove(0)

  if len(res) == 0 or len(res) > 2:
    return 'not possible'
  
  # code goes here
  return ",".join([str(num) for num in sorted(res)])

# keep this function call here 
print(ScaleBalancing(input()))
