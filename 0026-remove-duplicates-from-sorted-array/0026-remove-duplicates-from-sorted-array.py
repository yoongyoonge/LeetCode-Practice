class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # 반환하는 k 만큼의 요소 수만 nums에서 중요하다.
        # nums의 k 만큼의 요소는 상대적으로 순서를 유지하면서 중복이 없어야 한다.
        # nums의 나머지 요소는 중요하지 않다.
        
        # 예제 1
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j