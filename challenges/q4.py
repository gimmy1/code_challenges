'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
'''

def largest_non_adjacent(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    cache = [0 for a in arr]
    cache[0] = max(cache[0], arr[0])
    cache[1] = max(cache[0], arr[1])

    for i in range(len(arr)):
        num = arr[i]
        cache[i] = max(cache[i-2] + num, cache[i])
    return cache[-1]

# largest_non_adjacent([5, 1, 1, 5])