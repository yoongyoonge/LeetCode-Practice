class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            
            #print(nums[:i], nums[i+1:])
            
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
            if i == (len(nums) - 1):
                return -1
                    
        # 예제 1
        """
        leftSum, rightSum = 0, sum(nums)
        for idx, ele in enumerate(nums):
            rightSum -= ele
            if leftSum == rightSum:
                return idx      
            leftSum += ele
        return -1       
        """