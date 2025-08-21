# Solution : https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/3649636/3-method-s-c-java-python-beginner-friendly/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_substring = set()
        max_length = 0 
        left_pointer = 0

        for right_pointer in range(len(s)): 
            if s[right_pointer] not in current_substring : 
                current_substring.add(s[right_pointer])
                max_length = max(max_length, right_pointer - left_pointer + 1)
            
            else : 
                while s[right_pointer] in current_substring : 
                    current_substring.remove(s[left_pointer])
                    left_pointer += 1
                current_substring.add(s[right_pointer])

        return max_length ##