class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        return [list(nums1-nums2), list(nums2-nums1)]
        
        # 예제 1
        """
        set1=set(nums1)
        set2=set(nums2)
        res=[[],[]]

        for i in set1:
            if i not in set2:
                res[0].append(i)
        for i in set2:
            if i not in set1:
                res[1].append(i)
        return res
        """
        
        # 예제 2
        """
        set1,set2=set(nums1),set(nums2)
        return[set1-set2,set2-set1]
        """