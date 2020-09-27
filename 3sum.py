# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

class Solution():
    def findTriplets(self, nums):
        nums = sorted(nums)
        output = set()

        for i in range(len(nums)-2):
            head = i + 1
            tail = (len(nums)-1)

            while nums[i] < 0 and head < tail:
                temp = nums[i] + nums[head] + nums[tail]

                if temp == 0:
                    output.add((nums[i], nums[head], nums[tail]))
                    if head == tail:
                        break
                if temp < 0:
                    head += 1
                else:
                    tail -= 1
        return output


a = Solution()
print(a.findTriplets([-1, 0, 1, 2, -1, -4]))
