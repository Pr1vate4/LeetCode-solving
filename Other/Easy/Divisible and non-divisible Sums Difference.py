#в среднем думал дольше чем над обычной
class Solution(object):
    def differenceOfSums(self, n, m):
        count_1 = 0
        count_2 = 0
        for i in range(n + 1):
            if i % m == 0:
                count_1 += i
                continue
            count_2 += i
        return count_2 - count_1      