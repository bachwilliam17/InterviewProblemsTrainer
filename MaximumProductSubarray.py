class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # use current min and max
        cur_min, cur_max = 1, 1
        sol = max(nums)

        for num in nums : 
            temp = cur_min * num
            cur_min = min(cur_min * num, cur_max * num, num)
            cur_max = max(temp, cur_max * num, num)

            sol = max(sol, cur_max)

        return sol