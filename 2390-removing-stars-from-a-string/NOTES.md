​1. remove 와 pop, del 차이
- remove는 지우고 싶은 '값'을 입력
- pop과 del은 index를 받아 지우는 것은 동일하지만 pop은 지워진 값을 반환하는 반면 del은 반환하지 않음
- pop에 아무값도 입력하지 않으면 마지막 항목을 삭제하고 돌려줍

``` python
a = [1,2,1,3,4,5,1]

#1) 
a.remove(1)

print(a)
print(a[0])
# [2, 1, 3, 4, 5, 1]
# 2

#2)
removed = a.pop(1)

print(a) 
print(removed) 
print(a[0])


# [1, 1, 3, 4, 5, 1] 
# 2 
# 1


# 3)
del a[1]

print(a) 
print(a[0])

# [1, 1, 3, 4, 5, 1] 
# 1
```

- 또한 del은 pop()과 다르게 리스트의 범위를 지정해 삭제할 수 있음
``` python
a = [1,2,1,3,4,5,1]
del a[:2]

print(a)

# [1, 3, 4, 5, 1]
```