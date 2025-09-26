class Solution(object):
    def validTree(self, n, edges):

        graph = { i:[] for i in range(n) }
        for n1, n2 in edges : 
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()

        def dfs(node, prev) : 
            if node in visited : 
                return False
            
            visited.add(node)
            for other in graph[node] : 
                if other == prev : 
                    continue
                if not dfs(other, node) : 
                    return False
                
            return True
        
        return dfs(0, -1) and len(visited) == n
        

            