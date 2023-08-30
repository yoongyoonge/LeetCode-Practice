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
                    res += (roman_dict[cur]-2*pre)
                else:
                    res += roman_dict[cur]

            pre = roman_dict[cur]

            
        
        return res
