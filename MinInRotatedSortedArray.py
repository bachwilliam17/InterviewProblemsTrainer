class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l, r = 0, len(nums) - 1

        while True : 
            m = (l + r) // 2 

            if m == 0 : 
                return nums[m]
            
            if nums[m - 1] < nums[m] : 
                if nums[m] > nums[r] :  
                    l = m + 1
                else : 
                    r = m - 1

            else : 
                return nums[m]

            