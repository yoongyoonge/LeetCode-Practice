class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = []
        max_cnt = max(candies)
        #print(max_cnt)
        for i in range(0, len(candies)):
            if (candies[i] + extraCandies) < max_cnt:
                result.append(0)
            else:
                result.append(1)

                
        return result
            