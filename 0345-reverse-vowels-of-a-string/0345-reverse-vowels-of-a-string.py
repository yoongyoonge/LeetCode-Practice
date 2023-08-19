class Solution:
    def reverseVowels(self, s: str) -> str:
        
        
        vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        find_vowels = []
        
        for char in s:
            if char in vowels_list:
                find_vowels.append(char)
        
        reverse_vowels = list(reversed(find_vowels))
        tmp_s = list(s)
        
        for i in range(len(tmp_s)):
            if tmp_s[i] in vowels_list:
                tmp_s[i] = reverse_vowels.pop(0)
                
        result = ''.join(tmp_s)
        return result