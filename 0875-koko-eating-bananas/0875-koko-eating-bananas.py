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
        ''' # 시간 제한 초과
    
  
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
    
    
    
        # 예제 3
        '''
        l,r=1,max(piles)
        while l<r:
            mid,t=(l+r)//2,0
            for i in piles: t+=(i+mid-1)//mid
            print(t,mid,end=" ")
            if t<=h:r=mid
            else:l=mid+1
        return l 
        '''