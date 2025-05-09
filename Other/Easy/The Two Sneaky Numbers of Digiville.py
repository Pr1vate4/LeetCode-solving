#очень легкая задачка
class Solution(object):
    def getSneakyNumbers(self, nums):
        arr = []
        for i in range(len(nums) - 2):
            b = nums.count(i)
            if b == 2:
                arr.append(i)
        return arr
        
