# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco e t a " , etc.)

class Solution(object):
    def palindromPermutation(self,str):
        str = ' '.join(str.lower())
        lst = [0]*256
        for x in range(len(str)):
            lst[ord(str[x])] += 1

        odd = 0
        for x in range(len(lst)):
            if lst[x] % 2 != 0:
                odd += 1
            if odd > 1:
                return False
        return True

obj = Solution()
print(obj.palindromPermutation("Tact Coa Bbb u"))
