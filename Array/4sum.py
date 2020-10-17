# Given an array nums of n integers and an integer target, are there elements a, b, c, and d
# in nums such that a + b + c + d = target? Find all unique quadruplets in the array which
# gives the sum of target.

# Note:
# The solution set must not contain duplicate quadruplets.
# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        output = set()
        length = len(nums)

        for i in range(length-3):
            for j in range(i+1, length-2):
                head = j + 1
                tail = length-1

                while head < tail:
                    temp = nums[i] + nums[j] + nums[head] + nums[tail]
                    if temp == target:
                        output.add((nums[i], nums[j], nums[head], nums[tail]))
                        head += 1
                        tail -= 1

                    if temp < target:
                        head += 1
                    elif temp > target:
                        tail -= 1

                    if head == tail:
                        break
        return output


a = Solution()
print(a.fourSum([-1, 0, 1, 2, -1, -4], -1))
