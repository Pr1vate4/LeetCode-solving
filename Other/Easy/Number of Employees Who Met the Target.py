#даже не прочитал условие, число на инпуте - аутпуте понял
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count = 0
        for i in hours:
            if target <= i:
                count += 1
        return count