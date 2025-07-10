class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_substring = {}

        current_max = 0
        max_seen = 0

        for index, letter in enumerate(s) :

            if letter in current_substring : 
                if len(current_substring) > current_max : 
                    max_seen = len(current_substring)
                current_max = 0
                current_substring = {}
                continue

            else : 
                current_max += 1
                current_substring[index] = letter

        if current_max > max_seen : 
            max_seen = current_max
        
        return max_seen