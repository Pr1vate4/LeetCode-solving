# 
class Solution(object):
    def interpret(self, command):
        res = command.replace("()", "o")
        result = res.replace("(al)", "al")
        return result