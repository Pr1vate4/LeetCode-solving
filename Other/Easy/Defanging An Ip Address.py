#было бы интересно, если бы не знал функцию реплейс
class Solution(object):
    def defangIPaddr(self, address):
        a=address.replace('.','[.]')
        return a
        