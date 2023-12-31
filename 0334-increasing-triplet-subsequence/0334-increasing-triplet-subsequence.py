class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        result = False

        first = second = float('inf') # 키포인트
        
        for i in range(0, len(nums)):
            if first >= nums[i]:
                first = nums[i]
            elif second >= nums[i]:
                second = nums[i]
            else:
                result = True

        return result
            
        
        #Time Limit Exceeded
        """
        prefix_list = []
        postfix_list = []
        result = False
        
        if len(nums) >= 3:
            for i in range(1, (len(nums)-1)):

                prefix_list = set(nums[:i])
                postfix_list = set(nums[(i+1):])
                
                min_value = min(prefix_list)
                max_value = max(postfix_list)
                
                if nums[i] > min_value and nums[i] < max_value:
                    result = True
                    break

        return result
        """
        
            