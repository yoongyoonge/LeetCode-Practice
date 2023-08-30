class Solution:
    def romanToInt(self, s: str) -> int:

        # I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000

        roman_dict = {
            "I": 1
            , "V": 5
            , "X": 10
            , "L": 50
            , "C": 100
            , "D": 500
            , "M": 1000
        }

        pre, res = 0, 0
        for cur in s:
            if pre == 0: 
                res += roman_dict[cur]
            else:
                if pre < roman_dict[cur]:
                    res += (roman_dict[cur]-2*pre) # 예제를 보니 굳이 이렇게 안해도 되겠구나 뒷 문자가 더 크면 그냥 답에서 빼주면 된다.
                else:
                    res += roman_dict[cur]

            pre = roman_dict[cur]

            
        
        return res


        # 예제 1
        '''
        m = roman_dict

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]

        return ans
        '''