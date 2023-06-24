# 输入：nums = [2,7,11,15], target = 9
# [0,1]
def twoSum1(nums, target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                # print('[i,j]')
                return[i,j]
def twoSum2(nums, target):
    hash = {}
    for i, num in enumerate(nums):
        if target - num in hash:
            return [hash[target - num], i]
        hash[nums[i]] = i
    return []
if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(twoSum1(nums,target))
    print(twoSum2(nums, target))
