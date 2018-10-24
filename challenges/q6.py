"""Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2"""

def running_median(nums):
    if len(nums) == 1:
        return nums[0]
    
    sort = []
    mean = []
    for i in range(len(nums)):
        sort.append(nums[i])
        if i % 2 == 0:
            # this means that you will pick the middle number
            if i == 0:
                mean.append(sort[i])
            else:
                sort = sorted(sort)
                idx = len(sort)//2
                mean.append(sort[idx])
                # mean.append((len(sort)) // 2)
        if i % 2 != 0:
            # this means that we will have to compute avg of middle numbers
            if i == 1:
                mean.append((sum(sort))/2)
            else: 
                sort = sorted(sort)
                idx = len(sort) // 2
                # import pdb; pdb.set_trace()
                mid_sum = (sort[idx] + sort[idx - 1]) / 2
                mean.append(mid_sum)
    return mean






print(running_median([2, 1, 5, 7, 2, 0, 5]))    