# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example 1:

# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

class Solution():
    def partitionLabels(self, s):
        last = {c: i for i, c in enumerate(s)}

        point = 0
        anchor = 0

        res = []

        for i, c in enumerate(s):
            point = max(point, last[c])
            if i == point:
                i = i-anchor + 1
                anchor = point + 1
                res.append(i)
        return res


a = Solution()
print(a.partitionLabels("ababcbacadefegdehijhklij"))
