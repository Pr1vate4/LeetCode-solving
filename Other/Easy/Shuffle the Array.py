# решение классное, подумать немного пришлось
class Solution(object):
    def shuffle(self, nums, n):
        res = []
        for i in range(len(nums)):
            if i + n >= len(nums):
                return res
            res.append(nums[i])
            res.append(nums[i + n])