#немного подумал
class Solution(object):
    def maximumWealth(self, accounts):
        res = 0
        for i in range(len(accounts)):
            count = 0
            for j in accounts[i]:
                count += j
            if count > res:
                res = count
        return res
            