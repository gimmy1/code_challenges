"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

def max_contiguous_sum(nums):
    c_sum, max_sum = 0, 0
    for num in nums:
        c_sum += num
        if c_sum < 0:
            c_sum = 0
            max_sum = 0
        else: 
            max_sum = c_sum
    
    return max_sum


print(max_contiguous_sum([34, -50, 42, 14, -5, 86]))