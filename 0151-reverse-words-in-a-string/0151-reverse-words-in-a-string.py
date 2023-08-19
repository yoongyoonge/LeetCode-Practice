class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split()
        reverse_s = list(reversed(s))
        
        return ' '.join(reverse_s)