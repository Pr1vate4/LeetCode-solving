#решил с первого раза без подсказок, вроде сложная, но если включить голову то сложной она перестанет быть
class Solution(object):
    def longestConsecutive(self, nums):
        count = 1
        maxi = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                i += 1
                continue
            if nums[i] == nums[i - 1] + 1:
                if count > maxi:
                    maxi = count
                count += 1
                i += 1
                continue
            else:
                count = 1
            i += 1 
            
        if maxi > 0:
            return maxi + 1
        if len(nums) == 1:
            return 1
        if len(nums) < 1:
            return 0
        return 1