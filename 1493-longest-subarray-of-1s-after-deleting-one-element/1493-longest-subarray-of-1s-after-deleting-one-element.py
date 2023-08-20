class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 1004 번 문제 공부한 후 연계
        i = 0
        zero_cnt = 1
        for j in range(len(nums)):
            zero_cnt -= 1 - nums[j]
            
            #print(i, j, zero_cnt)
            
            if zero_cnt < 0:
                zero_cnt += 1 - nums[i]
                i+=1
                
        
        return j-i
        
        # 예제 1
        """
        longest = prev = curr = 0

	    for bit in nums:
	    	if bit:
	    		curr += 1
	    		longest = max(longest, prev + curr)
	    	else:
	    		prev, curr = curr, 0
    
	    return longest - (longest == len(nums))
        """
        
        # 예제 2
        """
        n = len(nums)

        left = 0
        zeros = 0
        ans = 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1 - zeros)

        return ans - 1 if ans == n else ans
        """