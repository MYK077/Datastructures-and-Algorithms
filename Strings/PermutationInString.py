# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.

# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

import collections


class Solution:
    def checkInclusion(self, s1, s2):
        dic1 = collections.Counter(s1)
        dic2 = collections.Counter(s2[:len(s1)])

        if dic1 == dic2:
            return True

        for i in range(1, len(s2)-len(s1)+1):
            if s2[i+len(s1)-1] in dic2:
                dic2[s2[i+len(s1)-1]] += 1
            else:
                dic2[s2[i+len(s1)-1]] = 1

            dic2[s2[i-1]] -= 1

            if dic2[s2[i-1]] == 0:
                del dic2[s2[i-1]]

            if dic1 == dic2:
                return True
        return False


a = Solution()
print(a.checkInclusion("ab", "eibas"))
