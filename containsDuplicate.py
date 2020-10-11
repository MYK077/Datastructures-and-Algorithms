class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # hashtable = Counter(nums)
        # for key,value in hashtable.items():
        #     if value >=2:
        #         return True
        # return False
        nums = sorted(nums)
        for x in range(len(nums)-1):
            if nums[x] == nums[x+1]:
                return True
        return False