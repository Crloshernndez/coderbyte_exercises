"""
Correct Path
Have the function CorrectPath(str) read the str parameter being passed, which will represent the movements made
in a 5x5 grid of cells starting from the top left position. The characters in the input string will be entirely
composed of: r, l, u, d, ?. Each of the characters stand for the direction to take within the grid,
for example: r = right, l = left, u = up, d = down. Your goal is to determine what characters the question marks
should be in order for a path to be created to go from the top left of the grid all the way to the bottom right
without touching previously travelled on cells in the grid.

For example: 
if str is "r?d?drdd" then your program should output the final correct string that will allow a path to be formed
from the top left of a 5x5 grid to the bottom right. For this input, your program should therefore return the string
rrdrdrdd. There will only ever be one correct path and there will always be at least one question mark within the
input string.

Examples
  Input: "drdr??rrddd?"
  Output: drdruurrdddd

  Input: "???rrurdr?"
  Output: dddrrurdrd

  Input: "rd?u??dld?ddrr"
  Output: rdrurrdldlddrr

  Input: "dddd?uuuurrr????"
  Output: ddddruuuurrrdddd

  Input: "ddr?rdrrd?dr"
  Output: ddrurdrrdldr

  Input: "rdrdr??rddd?dr"
  Output: rdrdruurdddldr

  Input: "???rrurdr?"
  Output: dddrrurdrd
"""

import itertools
import time

def CorrectPath(str):
    moves = {'r':(0,1), 'l':(0,-1), 'd':(1,0), 'u':(-1,0)}
    
    unknown_moves = str.count('?')
    
    for permutation in itertools.product(moves.keys(), repeat=unknown_moves):
        permutation = list(permutation)
        
        path=''
        pos = (0, 0)
        visited = [pos]

        for move in list(str):
            if move == '?': move = permutation.pop()
            path += move
            pos = tuple(sum(x) for x in zip(pos, moves[move]))

            if pos in visited: break
            if max(pos) > 4 or min(pos) < 0: break

            visited.append(pos)

        else:
            if pos == (4,4):
                return path
                
# keep this function call here 
start_time = time.time()
print(CorrectPath("rd?u??dld?ddrr"))
end_time = time.time()
execution_time = end_time - start_time
print("Tiempo de ejecución:", execution_time, "segundos")