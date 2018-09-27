"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [5, 4, 3, 10], the expected output would be [2, 3, 6].

Without Division
"""
def productOfAllButN(arr):
    # get product of all numbers before i and store in arr for easy access
    prefix = []
    for a in arr:
        prefix.append(a) if not prefix else prefix.append(prefix[-1] * a)
    
    rev_arr = reverse_array(arr)
    suffix = []
    for a in rev_arr:
        suffix.append(a) if not suffix else suffix.append(suffix[-1] * a)
    
    suffix = list(reversed(suffix))

    result = []
    for i in range(len(arr)):
        if i == 0:
            # first item should be product of all nums infront of 0th element [suffix] - is 2nd to last item (remember not using product of last item)
            result.append(suffix[i+1])
        elif i == len(arr)-1:
            # last item should be product of all nums before n-1th element [prefix] - is 2nd to last item (remember not using product of last item)
            result.append(prefix[i-1])
        else: 
            result.append(prefix[i-1] * suffix[i+1])
    return result

def reverse_array(arr):
    for i in range(len(arr)// 2): # divide with // to avoid floating numbers
        tmp = arr[i]
        arr[i] = arr[len(arr) - i - 1]
        arr[len(arr) - i - 1] = tmp
    return arr


print(productOfAllButN([1, 2, 3, 4, 5]))



