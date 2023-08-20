class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # 예제 1
        """
        left = 0
        answer = 0
        counts = {0: 0, 1: 0}
        
        for right, num in enumerate(nums):
            counts[num] += 1
            
            while counts[0] > k:
                counts[nums[left]] -= 1
                left += 1
                
            curr_window_size = right - left + 1
            answer = max(answer, curr_window_size)
            
        return answer
        """
    
        # 예제 2
        """
        left, right = 0, 0    
        for right in range(len(nums)):
            #print(nums[left], nums[right])
            #print(left, right, k)

            if nums[right] == 0:
                k-=1
            if k<0:
                if nums[left] == 0:
                    k+=1
                left+=1
        return right-left+1
        """
        
        # 예제 3
        
        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j] # k = k - (1 - nums[j])
            print(nums[j])
            print(i, j, k)
            
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1
        