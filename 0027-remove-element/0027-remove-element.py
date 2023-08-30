class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        index = 0

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[index] = nums[i] # 같지 않은 것만 차곡차곡 모으면 되는구나
                index += 1

        return index
                