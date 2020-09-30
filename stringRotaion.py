# String Rotation; Assume you have a method i s S u b s t r i n g which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to i s S u b s t r i n g [e.g., "water b o t t l e " is a rotation o P ' e r b o t t l e w a t " ),

class Solution(object):
    def rotateString(self, A, B):

        # Check if sizes of two strings are same
        if len(A) != len(B):
            return 0

        if B in (A+A):
            return True


obj = Solution()
print(obj.rotateString('abcde', 'cdeab'))
