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
    
        # 예제 1
        """
        s = list(s)
        left = 0
        right = len(s) - 1
        m = 'aeiouAEIOU'
        while left < right:
            if s[left] in m and s[right] in m:
                
                s[left], s[right] = s[right], s[left]
                
                left += 1; right -= 1
            
            elif s[left] not in m:
                left += 1
            
            elif s[right] not in m:
                right -= 1
            
        return ''.join(s)
        """