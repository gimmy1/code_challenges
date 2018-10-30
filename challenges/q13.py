

def threeNumSum(nums, k):
    nums.sort()
    triplets = []
    for i in range(len(nums)-2): # can't go allll the way, you know
        left = i+1
        right = len(nums) - 1
        while left < right:
            currSum = nums[i] + nums[left] + nums[right]
            if currSum == k:
                triplets.append(nums[i], nums[left], nums[right])
                left += 1
                right -= 1
            elif currSum < k:
                left += 1
            elif currSum > k:
                right += 1
        
    return triplets

