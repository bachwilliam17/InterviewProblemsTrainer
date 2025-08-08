class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sol = len(nums)

        for i in range(len(nums)) : 
            sol += (i - nums[i])

        return sol