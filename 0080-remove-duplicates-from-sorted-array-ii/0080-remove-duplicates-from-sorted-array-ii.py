class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 0 # 배열의 k번째 값을 업데이트 하기 위한 변수

        for i in nums:
            if k < 2 or i != nums[k-2]:
                nums[k] = i
                k += 1
        return k
            
        
