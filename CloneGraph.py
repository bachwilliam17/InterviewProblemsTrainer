"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        newGraph = {}

        def dfs(node) : 
            if node in newGraph :
                return newGraph[node]
            
            newNode = Node(node.val)
            newGraph[node] = newNode
            
            for neighbor in node.neighbors : 
                newNode.neighbors.append(dfs(neighbor))
            
            return newNode
        
        return dfs(node) if node else None
