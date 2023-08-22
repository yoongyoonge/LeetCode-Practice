class Solution:
    def removeStars(self, s: str) -> str:
        
        list_s = list(s)
        result = []
        for i in range(len(list_s)):
            if list_s[i] == "*":
                result.pop(-1)
            else:
                result.append(list_s[i])
        return ''.join(result)
    
        # 예제 1
        """
        ans=[]
        for i in s:
            if i=='*':
                ans.pop()
            else:
                ans+=[i]
        return "".join(ans)
        """
        
        # 예제 2
        """
        res = []
        for i in s:
            if i != '*':
                res.append(i)
            elif res:
                res.pop()
        return ''.join(res)
        """