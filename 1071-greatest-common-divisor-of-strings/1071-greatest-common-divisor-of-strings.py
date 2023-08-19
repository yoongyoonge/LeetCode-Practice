class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        ### 좋은 아이디어가 안떠올라서 다른사람 코드 복붙..
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]
