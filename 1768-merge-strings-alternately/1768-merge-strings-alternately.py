class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = ""
        iter_int = 0
        for i, j in zip(word1, word2):
            result = result + i + j
            iter_int += 1

        result = result + word1[iter_int:] + word2[iter_int:]

        return result
        
        
        # 다른 풀이 1
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)
        """
        
        # 다른 풀이 2
        """
        result = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]

        return "".join(result)
        """