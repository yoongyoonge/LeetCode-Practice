class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        ### 좋은 아이디어가 안떠올라서 다른사람 코드 복붙..
        ### 반복되는지 체크한 후에 최소 공약수를 구해서 그만큼 문자열에서 추출
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]
