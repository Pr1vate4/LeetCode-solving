#оч крутая задачка
class Solution(object):
    
    def convertDateToBinary(self, date):
        a,b,c = date.split('-')
        it = []
        a,b,c = int(a),int(b),int(c)
        return bin(a)[2:] + "-" + bin(b)[2:] + "-" + bin(c)[2:]