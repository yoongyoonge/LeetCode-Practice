class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        from collections import Counter
        
        a = sorted(Counter(arr).values())
        
        for i in range(0, len(a)-1):
            if a[i] == a[i+1]:
                return False
                
        return True
    
    # 예제 1
    """
    return (lambda x: len(x) == len(set(x)))(collections.Counter(A).values())
    """
    
    # 예제 2
    """
    from collections import Counter
    cnt = Counter(arr)     
    x = cnt.values()
    y = set(x)
    return len(x) == len(y)
    """