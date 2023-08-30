class Solution:
    def reverseWords(self, s: str) -> str:

        l_s = reversed(s.split())

        return ' '.join(l_s)