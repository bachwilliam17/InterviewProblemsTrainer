class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums = nums.sort()
        sol = []

        for idx, num in enumerate(nums) :
            if idx > 0 and num == nums[idx - 1] : 
                continue

            l, r = idx + 1, len(nums) - 1
            while l < r : 
                sum = num + nums[l] + nums[r]

                if sum > 0 : 
                    r -= 1

                elif sum < 0 : 
                    l += 1

                else : 
                    sol.append(num, nums[l], nums[r])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r :
                        l += 1
            
            return sol


