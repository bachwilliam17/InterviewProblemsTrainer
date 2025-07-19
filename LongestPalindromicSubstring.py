class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for length in range(2, n + 1) : 
            for i in range(n) 