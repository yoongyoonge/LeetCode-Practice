class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            
            #print(nums[:i], nums[i+1:])
            
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
            if i == (len(nums) - 1):
                return -1
                    
                