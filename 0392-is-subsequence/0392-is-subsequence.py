class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        list_s = list(s)
        list_t = list(t)
        s_index = 0
        
        result = False
        
        if len(list_s) == 0:
            return True
        
        for i in range(0, len(list_t)):

            if list_s[s_index] == list_t[i] :
                s_index += 1
                
                if s_index == len(list_s):
                    return True
                    
        return result
    
        # 예제 1
        """
        for c in s:
            i = t.find(c)
            if i == -1:    return False
            else:   t = t[i+1:]
        return True
        """
            