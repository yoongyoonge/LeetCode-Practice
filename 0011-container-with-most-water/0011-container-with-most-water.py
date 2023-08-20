class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Time Limit Exceeded
        """
        max_store = 0
        for i in range(0, len(height)):
            for j in range(i, len(height)):
                
                if height[i] <= height[j]:
                    cal_store = height[i] * (j-i)
                else:
                    cal_store = height[j] * (j-i)
                    
                max_store = max(max_store, cal_store)
                
        return max_store
        """
        
        # 예제 1
        """
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
        """
        
        # 예제 2
        
        l, r, area = 0, len(height) - 1, 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
				
        return area
        