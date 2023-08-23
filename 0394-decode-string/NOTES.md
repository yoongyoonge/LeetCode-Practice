​1. isdigit()
- 문자열이 숫자인지 판별하는 함수
- 알파벳인지 확인하는 함수는 isalpha()
- 알파벳, 숫자 모두 확인하고 싶으면 isalnum()

``` python
# Example for isdigit

ex_01 = '123'
ex_02 = '010-1234-5678'
ex_03 = "전화번호010"
ex_04 = "Phone 010"

# print result of isdigit()

print(ex_01.isdigit())
print(ex_02.isdigit()) # 기호가 포함되여 False
print(ex_03.isdigit()) # 문자가 포함되어 False
print(ex_04.isdigit()) # 공백이 포함되어 False
```