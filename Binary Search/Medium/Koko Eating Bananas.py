#на этой задаче понял, что нужно сначало изучить бинарный поиск,(думал над ней 2 часа) пока не рабочий код, который в теории работает
class Solution(object):
    def minEatingSpeed(self, piles, h):
        count = 0
        
        
        for k in range(min(piles),max(piles) + 1):
            count = 0
            for i in range(len(piles)):
                if piles[i] <= k:
                    count += 1
                    continue
                while piles[i] - k > 0:
                    piles[i] = piles[i] - k 
                    count += 1
                count += 1
            
            
            if count <= h:
                return k
            