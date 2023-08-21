class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        l_word1 = list(word1)
        l_word2 = list(word2)
        
        if set(l_word1) != set(l_word2):
            return False
        
        from collections import Counter
        
        c_word1 = Counter(l_word1).values()
        c_word2 = Counter(l_word2).values()
        
        if sorted(c_word1) == sorted(c_word2):
            return True
        
        return False