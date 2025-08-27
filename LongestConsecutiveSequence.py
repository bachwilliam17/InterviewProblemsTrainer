class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max = 0 
        numsSet = set(nums)

        for num in numsSet : 
            if (num - 1) not in numsSet : 
                length = 0
                while (num + length) in numsSet :
                    length += 1

                max = max(max, length) 

        return max

