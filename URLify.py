# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr 3ohn Smith
# Output: "Mr%203ohn%20Smith

class Solution(object):
    def urlify(self,s):
        words = s.split()
        url= ''
        pointer = 0
        for x in words:
            if pointer < len(words)-1:
                url = url + x + "%20"
                pointer+=1
            else:
                return url
obj = Solution()
print(obj.urlify("myk ydv jonh wick jason free human                 "))
