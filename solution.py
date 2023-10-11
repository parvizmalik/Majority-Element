

def majorityNum(nums):
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if candidate==num else -1)    
    return candidate


print(majorityNum([3,2,3]))
