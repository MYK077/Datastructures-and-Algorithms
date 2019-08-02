# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# p a l e , pie -> true
# p a l e s , pale -> true
# p a l e , bale -> true
# p a l e , bake -> false

class Solution(object):
    def oneAway(self, str1, str2):
        length1 = len(str1)
        length2 = len(str2)
        if abs(length1 -  length2) > 1:
            return False
# to count the edits
        count = 0
# initialize x and y equal to zero
        x = 0
        y = 0
        while x < length1 and y < length2:
            if str1[x] != str2[y]:
                if count == 1:
                    return False
                elif length1 < length2:
                    x += 1
                elif length2 < length1:
                    y += 1
                else:
                    x += 1
                    y += 1
                count += 1
            else:
                 x += 1
                 y += 1

        return True


obj = Solution()
print(obj.oneAway('pale','paleds'))

# x = 0
# y = 0
# lst1 = []
# lst2 = []
# while x < 10 and y < 20:
#     lst1.append(x)
#     lst2.append(y)
#     y += 1
#     x += 1
#
# print(lst1)
# print(lst2)
