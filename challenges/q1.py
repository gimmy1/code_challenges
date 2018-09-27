"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
from sys import argv
def twoNumSum(arr, value):
    differences = {}
    for a in arr:
        difference = value - a
        if difference in differences:
            return True
        else: 
            differences[a] = True
    return False

argv1 = list(argv[1])
result = []
for i in argv1:
    try:
        result.append(int(i))
    except ValueError:
        # import pdb; pdb.set_trace()
        continue
argv2 = int(argv[2])
# print(type(argv2))
print(twoNumSum(result, argv2))
# print(twoNumSum([10, 15, 3, 8], 18))