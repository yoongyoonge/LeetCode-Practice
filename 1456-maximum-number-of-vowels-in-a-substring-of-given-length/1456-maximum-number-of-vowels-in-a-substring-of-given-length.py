class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowel_list = "aeiou"
        list_s = list(s)
        
        tmp_list = list_s[0:k]
        
        cnt = 0
        for val in tmp_list:
            if val in vowel_list:
                cnt += 1
        
        max_cnt = cnt
        
        for i in range(k, len(list_s)):
            prev = tmp_list.pop(0)
            tmp_list.append(list_s[i])
            
            if prev in vowel_list:
                cnt -= 1
            
            if tmp_list[k-1] in vowel_list:
                cnt += 1

            max_cnt = max(max_cnt, cnt)
        
        return max_cnt
    
        # 예제 1
        """
        vowels = frozenset("aeiou")
        cnt = ans = sum(s[i] in vowels for i in range(k))
        if ans != k:
            for i in range(k, len(s)):
                cnt += (s[i] in vowels) - (s[i - k] in vowels)
                if (ans := max(cnt, ans)) == k:
                    break
        return ans
        """
        
        # 예제 2
        """
        vowels = frozenset("aeiou")
        cnt = ans = sum(s[i] in vowels for i in range(k))
        if ans != k:
            for i in range(k, len(s)):
                cnt += (s[i] in vowels) - (s[i - k] in vowels)
                ans = max(cnt, ans)
        return ans
        """
        
        # 예제 3
        """
        vowels = frozenset("aeiou")
        cnt = ans = sum(s[i] in vowels for i in range(k))
        for i in range(k, len(s)):
            cnt += (s[i] in vowels) - (s[i - k] in vowels)
            ans = max(cnt, ans)
        return ans
        """