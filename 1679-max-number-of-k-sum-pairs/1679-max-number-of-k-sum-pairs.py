class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        # Time Limit Exceeded
        """
        base, pnt = 0, 1
        op_cnt = 0
        
        while base != (len(nums) - 1):
            
            if len(nums) < 1:
                break
            
            if ( nums[base] + nums[pnt] ) == k:
                nums.pop(base)
                nums.pop(pnt-1)
                pnt = base+1
                op_cnt += 1
            elif pnt != (len(nums)-1):
                pnt += 1
            else:
                base += 1
                pnt = base+1
                
            
        return op_cnt
        """
    
        # 예제 1
        """
        res, d = 0, Counter(nums)
        for val1, cnt in d.items():
            val2 = k - val1
            # it's trick to get rid of duplicates pairs, consider only pairs where val1 >= val2
            if val2 < val1 or val2 not in d: continue 
            res += min(cnt, d[val2]) if val1 != val2 else cnt//2
        
        return res
        """
        
        # 예제 2
        nums.sort()
        res, l, r = 0, 0 ,len(nums) - 1

        while l < r:
            S = nums[l] + nums[r]
            if S > k:
                r -= 1
            elif S < k:
                l += 1
            else:
                res += 1
                l += 1
                r -= 1
        return res