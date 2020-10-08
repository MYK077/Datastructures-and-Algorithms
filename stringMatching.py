# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".

class Solution:
    def stringMatching(self, words):
        string = ' '.join(words)


        substr = []
        for i in words:
            if string.count(i) >= 2:
                substr.append(i)
        return substr

a = Solution()
print(a.stringMatching(["mass","as","hero","superhero"]))