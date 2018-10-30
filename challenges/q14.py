"""
Function that takes in 2-non empty arrays of integers
Find two integers (from array 1 and 1 from array 2) whose absolute difference is closest to 0
"""

def find_smallest_difference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    curr = float("inf")
    smallestPair = []
    while idxOne <= len(arr1) and idxTwo <= len(arr2):
        first = arr1[idxOne]
        sec = arr2[idxTwo]
        
        if first < sec:
            curr = abs(first - sec)
            idxOne += 1
        
        elif sec < first:
            curr = abs(first-sec)
            idxTwo += 1
        
        else: 
            return smallestPair[first, sec]
        
        if smallest > curr:
            smallest = curr
            smallestPair = [first, sec]
    
    return smallestPair