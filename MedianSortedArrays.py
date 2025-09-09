# Solution : 

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # Recherche binaire sur le plus petit tableau
        A, B = nums1, nums2
        if len(A) > len(B) : 
            A, B = B, A 
        
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1 

        while True : 
            mA = l + r // 2
            # pointeur sur B déduit car on sait la taille de la partition
            mB = half - mA - 2 

            # Extrémités des partitions
            ALeft = A[mA] if mA >= 0 else float("-infinity")
            ARight = A[mA + 1] if mA + 1 < len(A) else float("infinity")
            BLeft = B[mB] if mB >= 0 else float("-infinity")
            BRight = B[mB + 1] if mB + 1 < len(B) else float("infinity")


            if ALeft <= BRight and BLeft <= ARight : 
                # partition trouvée (première moitié du tableau fusionné)
                if total % 2 :
                    return min(ARight, BRight) 
                else : 
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            
            elif ALeft > BRight : 
                r = mA - 1
            else : 
                l = mA + 1

            # best