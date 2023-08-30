class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        from collections import Counter

        cnt_num = Counter(nums)

        for key, value in cnt_num.items():
            if value > len(nums)//2:
                return key


        