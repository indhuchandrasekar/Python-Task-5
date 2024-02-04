# 2 Write a Python code using Lambda function to check every element of a List
# is an Integer or string?
from functools import reduce

test_list = [[5,6,3],["Gfg", 3, "is"],[9, "best", 4]]

print("The original list : " + str(test_list))

res = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, str)], test_list, [])

print("The string instances : " + str(res))

res1 = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, int)], test_list, [])

print("The integer instances : " + str(res1))