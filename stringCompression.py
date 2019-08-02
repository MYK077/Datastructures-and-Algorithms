# 1.6 String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3, If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
# O(n)
from collections import Counter
class Solution(object):
    def stringCompression(self,s):
        hashTable = Counter(s)
        emptyStr = ''
        for key,value in hashTable.items():
            value = str(value)
            emptyStr = emptyStr + key + value
        if len(emptyStr) < len(s):
            return emptyStr
        return s


obj = Solution()
print(obj.stringCompression("aaABBBaddhhhhh"))
