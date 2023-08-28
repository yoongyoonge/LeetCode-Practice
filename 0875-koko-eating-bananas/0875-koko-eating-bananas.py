class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # 예제 1
        '''
        k = 1 
        while True:
            total_time = 0
            for i in piles:
                total_time += ceil(i / k)
            if total_time > h:
                k += 1
            else:
                return k
        '''
    
  
        # 예제 2
        left = ceil(sum(piles) / h) # lower bound of Binary Search 
        right = max(piles) # upper bound of Binary Search 
        while left < right:
            mid = (left + right) // 2 # we check for k=mid
            total_time = 0
            for i in piles:
                total_time += ceil(i / mid)
                if total_time > h:
                    break
            if total_time <= h:
                right = mid # answer must lie to the left half (inclusive of current value ie mid)
            else:
                left = mid + 1 # answer must lie to the right half (exclusive of current value ie mid)
        return right