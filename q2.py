"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [5, 4, 3, 10], the expected output would be [2, 3, 6].

Without Division
"""
from functools import reduce
def productOfAllButN(arr):
    # Find the product before i
    prefix = []
    for a in arr:
        # iterate over array, append and multiply instead of running over and over again
        # multiplying bc we can quickly receive the product of everything before i
        prefix.append(a) if not prefix else prefix.append(prefix[-1] * a)
    
    
    rev_arr = reverse_arr(arr)
    # Find the product after i
    suffix = []
    for a in rev_arr:
        # iterate over array, append and multiply instead of running over and over again
        suffix.append(a) if not suffix else suffix.append(suffix[-1] * a)
    
    # import pdb; pdb.set_trace()
    suffix = list(reversed(suffix))
    
    result = []
    for i in range(len(arr)):
        # [10, 30, 120, 600]
        if i == 0:
            result.append(suffix[i+1])
        elif i == len(arr)-1:
            result.append(prefix[i-1])
        else:
            result.append(prefix[i-1] * suffix[i+1])
    return result

def reverse_arr(arr):
    for i in range(len(arr) // 2):
        tmp = arr[i]
        # import pdb; pdb.set_trace()
        arr[i] = arr[len(arr) - i - 1]
        arr[len(arr) - i - 1] = tmp
    return arr


print(productOfAllButN([3, 2, 1]))



