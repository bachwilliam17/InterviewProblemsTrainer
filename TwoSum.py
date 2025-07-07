class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result = []

        for index, current_num in enumerate(nums) : 

            for index2, other_num in enumerate(nums) : 
                
                sum_result = current_num + other_num
                if sum_result == target : 
                    result.append(index)
                    result.append(index2)
                    return result

