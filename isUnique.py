#
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures
#
# O(n^2)
class Solution(object):
    def isUnique(self, s):
        for x in range(len(s)):
            for j in range(x+1,len(s)):
                if s[x] == s[j]:
                    return False
        return True

string = Solution()
print(string.isUnique("st91065 65"))

# O(n log n)
class Solution(object):
    def isUnique(self, s):
        s = sorted(s)
        for x in range(len(s)):
            if x+1 == len(s):
                break
            if ord(s[x]) == ord(s[x+1]):
                return False
        return True

string = Solution()
print(string.isUnique("ustmkoiu"))
