#слишком легкая задачка                
class Solution(object):
    def minimumOperations(self, nums):
        count = 0
        for i in nums:
            if i % 3 == 0:
                continue
            count += 1
        return count
        