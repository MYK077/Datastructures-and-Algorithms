# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# p a l e , pie -> true
# p a l e s , pale -> true
# p a l e , bale -> true
# p a l e , bake -> false

# class Solution(object):
#     def oneAway(self, str1, str2):
#         length1 = len(str1)
#         length2 = len(str2)
#         if abs(length1 -  length2) > 1:
#             return False
# # to count the edits
#         count = 0
# # initialize x and y equal to zero
#         x = 0
#         y = 0
#         while x < length1 and y < length2:
#             if str1[x] != str2[y]:
#                 if count == 1:
#                     return False
#                 elif length1 < length2:
#                     y += 1
#                 elif length2 < length1:
#                     x += 1
#                 else:
#                     x += 1
#                     y += 1
#                 count += 1
#             else:
#                  x += 1
#                  y += 1
#         return True
#
#
# obj = Solution()
# print(obj.oneAway('pale','ple'))

class Solution(object):
    def oneAway(self, str1, str2):
        if abs(len(str1)-len(str2)) > 1:
            return False
        x = 0
        y = 0
        count = 0
        while x <= len(str1)-1 and y <= len(str2)-1:
            if str1[x] == str2[y]:
                x += 1
                y += 1
            elif str1[x] != str2[y] and len(str1) > len(str2):
                count += 1
                x += 1
            elif str1[x] != str2[y] and len(str2) > len(str1):
                count+=1
                y += 1
            else:
                x += 1
                y += 1
            if count > 1:
                return False
        return True

obj = Solution()
print(obj.oneAway('pale','palesd'))
