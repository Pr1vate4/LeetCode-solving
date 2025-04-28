#обычная легкая задачка
class Solution(object):
    def transformArray(self, nums):
        
        arr = []
        for i in nums:
            if i % 2 == 0:
                arr.append(0)
            else:
                arr.append(1)
        res = sorted(arr)
        return res
            