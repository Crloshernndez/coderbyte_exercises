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
print(BracketMatcher("the color re(d))()(()"))
