# solution : https://leetcode.com/problems/two-sum/solutions/737092/sum-megapost-python3-solution-with-a-detailed-explanation/

test = {}
test[25] = 5
test[30] = 6
print(test)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen ={}

        for index, current_num in enumerate(nums) : 

            remainder = target - current_num

            if remainder in seen : 
                return [index, seen[remainder]]
            else : 
                seen[current_num] = index

