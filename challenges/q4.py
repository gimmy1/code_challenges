'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
'''

def largest_non_adjacent(arr):
    if len(arr) <= 2:
        # import pdb; pdb.set_trace()
        return max(0, max(arr))
    
    # import pdb; pdb.set_trace()
    cache = [0 for i in arr] # array of 0's
    cache[0] = max(0, arr[0]) # first element in array
    cache[1] = max(cache[0], arr[1]) # first element in array

    for i in range(2, len(arr)):
        num = arr[i]
        cache[i] = max(num + cache[i-2], cache[i-1]) # create array of non-adjacent indices and their sum
    return cache[-1] 


largest_non_adjacent([5, 1, 1, 5])