"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [5, 4, 3    ], the expected output would be [2, 3, 6].

Without Division
"""
def productOfAllButN(nums):
    '''
    How?
    we can get the prefix/suffix product of the index
    '''
    prefix = []
    for num in nums:
        # [] is False == True
        if prefix:
            prefix.append(prefix[-1] * num)
        else:
            prefix.append(num)
    
    suffix = []
    rev_arr = reverse_arr(nums)
    for num in rev_arr:
        # [] is False == True
        if suffix:
            suffix.append(suffix[-1] * num)
        else:
            suffix.append(num)
    
    suffix = reverse_arr(suffix)
    productOfAll = []
    for i in range(len(nums)):
        if i == 0:
            import pdb; pdb.set_trace()
            # if it is this one you want this to equal to ALl of them except the first one! So we will use suffix
            productOfAll.append(suffix[i+1])
        elif i == len(nums) - 1:
            productOfAll.append(prefix[i-1])
        else:
            productOfAll.append(suffix[i+1] * prefix[i-1])
    
    return productOfAll


    # import pdb; pdb.set_trace()

def reverse_arr(arr):
    # need only go to the half way point, otherwise you will be reverse all the way to the end!!
    for i in range(len(arr) // 2):
        # import pdb; pdb.set_trace()
        tmp = arr[i]
        arr[i] = arr[len(arr) - i - 1]
        arr[len(arr) - i - 1] = tmp
    return arr



print(productOfAllButN([5, 4, 3]))



