# не понял что такое nums[nums[i]], но понял как с этим работать
class Solution(object):
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans
        