class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        from collections import Counter
        
        a = Counter(arr)
       
        a = sorted(a.values())
        print(a)
        
        for i in range(0, len(a)-1):
            if a[i] == a[i+1]:
                return False
                
        return True