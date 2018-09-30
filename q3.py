'''
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
'''

def first_missing_positive(arr):
    '''
    For now let us use PYthon's set
    '''
    arr_set = set(arr)
    # 1 can be considered the lowest value not in an array
    i = 1
    for i in arr_set:
        # if i in set then increment, if not - we can simply return i. 
        # Remember, must be sequential
        i += 1
    return i