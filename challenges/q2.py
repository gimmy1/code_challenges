"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [5, 4, 3, 10], the expected output would be [2, 3, 6].

Without Division
"""
def productOfAllButN(arr):
    # so what you wnt to do iss get the values of everything pre and post
    pre = []
    for a in arr:
        if pre:
            pre.append(pre[-1] * a)
        else: 
            pre.append(a)

    
    reverse_arr = reverse(arr)
    post = []
    for a in reverse_arr:
        if post:
            post.append(post[-1] * a)
        else: 
            post.append(a)
    
    post = reverse(post)
    
    product = []
    for i in range(len(arr)):
        import pdb; pdb.set_trace()
        if i == 0:
            product.append(post[i+1])
        elif i == len(arr)-1:
            product.append(pre[i-1])
        else:
            # import pdb; pdb.set_trace() 
            product.append(pre[i-1] * post[i+1])
    return product



def reverse(arr):
    for i in range(len(arr) // 2):
        # import pdb; pdb.set_trace()
        tmp = arr[i]
        arr[i] = arr[len(arr) - i - 1]
        arr[len(arr) - i - 1] = tmp
    return arr



