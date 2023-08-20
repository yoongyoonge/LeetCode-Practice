​
1. frozenset 이란?
    - frozenset과 set은 모든 문법과 기능이 거의 동일
    - mutable 하냐의 차이만 존재
    - set은 mutable 객체이고 frozenset은 immutable 객체

<br>

2. set 활용법
    - 저장순서를 유지하지 않고, 중복된 값의 저장을 허용하지 않는 set
    - 차집합: set1 - set2
    - 교집합: set1 & set2
    - 합집합: set1 | set2
    - 대칭 차집합((set1-set2) U (set2-set1)): set1 ^ set2

<br>

3. := 바다코끼리 연산자
    - python 3.8에 속함
    - 표현식에 이름을 부여하고 재사용할 수 있게 하는 것
    
    ``` python
    li=[] 
    for i in range(10):
    if i==0:
        start=i 
    if i==9:
        end=i 
    li.append(i) 
    print(li) 
    print(start,end) 
    
    #walrus operator
    li = [(end:=i) if i else (start:=i) for i in range(10)]
    print(li) 
    print(start, end) 
    ```
    
    - 단, 튜플에서 대입 연산자와 다르게 동작

    ``` python
    x = 1, 2 # x에 (1, 2)를 대입
    (x := 1, 2) # x에 1을 대입
    ```