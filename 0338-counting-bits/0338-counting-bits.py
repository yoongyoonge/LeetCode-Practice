class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        from collections import Counter
        for i in range(0, n+1):
            bin_i = bin(i)
            bin_i = Counter(bin_i)
            res.append(bin_i["1"])
            
        return res