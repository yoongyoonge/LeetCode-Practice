class Solution:
    def canJump(self, nums: List[int]) -> bool:

        cur = 0

        if len(nums) == 1 : return True # 문제 조건

        index = 0; jump = index
        for index in range(100000):
            if jump > index+nums[index]:pass
            else: jump = index+nums[index]

            index+=1

            if index > jump: break
            if jump >= len(nums)-1: return True 

        return False
