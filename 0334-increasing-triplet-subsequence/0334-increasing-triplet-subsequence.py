class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        result = False
        #first = nums[0]
        #second = nums[1]
        
        first = second = float('inf') 
        
        for i in range(0, len(nums)):
            if first >= nums[i]:
                first = nums[i]
            elif second >= nums[i]:
                second = nums[i]
            else:
                #if first < second and second < nums[i]:
                result = True
                
            print(first, second, nums[i])
            print(result)
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
        
            