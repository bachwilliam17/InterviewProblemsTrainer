class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid : 
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c) : 
            q = collections.deque() # type: ignore
            visited.add((r, c))
            q.append((r, c))

            while q : 
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions : 
                    r_adj, c_adj = row + dr, col + dc

                    if r_adj in range(rows) and c_adj in range(cols) and grid[r_adj][c_adj] == "1" and (r_adj, c_adj) not in visited :
                        q.append((r_adj, c_adj))
                        visited.add((r_adj, c_adj))

        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == "1" and (r, c) not in visited : 
                    islands += 1
                    bfs(r, c)

        return islands
                
