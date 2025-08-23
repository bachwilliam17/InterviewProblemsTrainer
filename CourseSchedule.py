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

        def dfs(crs) : 
            if crs in visited : 
                return False
            if preMap[crs] == [] : 
                return True
            
            visited.add(crs)
            for pre in preMap[crs] : 
                if not dfs(pre) : return False
            visited.remove(crs)
            preMap[crs] = []

            return True
        
        for i in range(numCourses) : 
            if not dfs(i) : return False
        return True