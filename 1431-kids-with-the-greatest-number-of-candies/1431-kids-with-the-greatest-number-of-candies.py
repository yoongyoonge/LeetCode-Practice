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
                
                
        ### 다른 풀이 1
        """
        maxCandies = max(candies)
	    result = []
	    for i in range(len(candies)):            
	    	result.append(candies[i]+extraCandies >= maxCandies)            
	    return result
        """


        ### 다른 풀이 2
        """
	    maxCandies = max(candies)
	    return [candy+extraCandies >= maxCandies for candy in candies]
        """
                
        return result
            