# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.
# O(1)
# from collections import Counter
# class Solution(object):
#     def permutation(self,str1, str2):
#         hashTable1 = Counter(str1)
#         hashTable2 =  Counter(str2)
#
#         if hashTable1 == hashTable2:
#             return True
#         return False
#
# obj = Solution()
# print(obj.permutation("abc","cba"))

class Solution(object):
    def permutation(self,str1, str2):
        hashTable1 = {}
        hashTable2 =  {}

        for x in str1:
            if x not in hashTable1:
                hashTable1[x] = 1
            else:
                hashTable1[x] += 1

        for x in (str2):
            if x not in hashTable2:
                hashTable2[x] = 1
            else:
                hashTable2[x] += 1

        if hashTable1 == hashTable2:
            return True
        return False

obj = Solution()
print(obj.permutation("abc","cbab"))
