class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        tmp_index = 0
        
        zero_cnt = nums.count(0)
        non_zero_cnt = int(len(nums) - zero_cnt)
        
        for j in range(len(nums)):
            if (nums[j] == 0) and (nums.index(0) != non_zero_cnt):
                tmp_index = nums.index(0)
                nums.append(nums.pop(tmp_index))
                
                #print(nums)
            
        
        # 예제 1
        """
        n = len(nums)
        i = 0
        for j in range(n):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        """