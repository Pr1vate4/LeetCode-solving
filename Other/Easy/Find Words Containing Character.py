#эта задачка мне понравилась, но лёгкая
class Solution(object):
    def findWordsContaining(self, words, x):
        arr = []
        for i in range(len(words)):
            for j in words[i]:
                if j == x:
                    arr.append(i)
                    break
        return arr