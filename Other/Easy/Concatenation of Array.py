#одна из самых легких зачач
class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for i in range(2):
            for i in nums:
                ans.append(i)
        return ans