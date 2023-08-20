class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        i = 0
        zero_cnt = 1
        for j in range(len(nums)):
            zero_cnt -= 1 - nums[j]
            
            #print(i, j, zero_cnt)
            
            if zero_cnt < 0:
                zero_cnt += 1 - nums[i]
                i+=1
                
        
        return j-i
            