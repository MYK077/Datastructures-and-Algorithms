# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

import sys


class Solution():
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        diff = sys.maxsize
        l = len(nums)

        for i in range(l-2):
            head = i + 1
            tail = l - 1

            while head < tail:
                temp = nums[i] + nums[head] + nums[tail]
                if abs(target - temp) < abs(diff):
                    diff = target - temp
                    if temp < target:
                        head += 1
                    else:
                        tail -= 1
            if diff == 0:
                break
        return target - diff


a = Solution()
print(a.threeSumClosest([-1, 2, 1, -4], 1))
