class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight) : 
            if (r, c) in visited or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight : 
                return
            
            visited.add((r,c))
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])

        for row in range(ROWS) : 
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLS - 1, atl, heights[row][COLS - 1])

        for col in range(COLS) : 
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])

        res = []
        for r in range(ROWS) : 
            for c in range(COLS) : 
                if (r, c) in pac and (r, c) in atl : res.append((r,c))

        return res
