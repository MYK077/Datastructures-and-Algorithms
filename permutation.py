# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.
# O(1)
from collections import Counter
class Solution(object):
    def permutation(self,str1, str2):
        hashTable1 = Counter(str1)
        hashTable2 =  Counter(str2)

        if hashTable1 == hashTable2:
            return True
        return False

obj = Solution()
print(obj.permutation("abc","cbad"))
