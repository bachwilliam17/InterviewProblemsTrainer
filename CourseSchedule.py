class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites : 
            preMap[crs].append(pre)

        visited = set()

        def dfs()