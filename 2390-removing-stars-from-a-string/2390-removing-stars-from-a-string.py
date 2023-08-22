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