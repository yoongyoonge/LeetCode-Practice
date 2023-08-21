​1. zip
- 두 리스트를 묶는 함수
- 여러 iterable 객체를 하나의 tuple로 통합

    ``` python
    name = ['merona', 'gugucon']
    price = [500, 1000]
    
    z = zip(name, price)
    print(list(z))
    
    # 출력
    # [('merona', 500), ('gugucon', 1000)]
    
    # 사용
    for n, p in zip(name, price):
        print(n, p)
    ```

- 두 개 이상도 묶을 수 있음

    ``` python 
    for node in zip(A, B, C):
    print(node)
    ```

- zip함수에 *args, **kargs를 인수로 넣을 수 있음
- 이러한 *(Asterisk)가 붙은 것은 가변 인자
    > *args : <br>
    > 파라미터를 몇개 받을지 모르는 경우에 사용한다. <br>
    > 튜플 형태로 전달된다.

    - 참고
    > **kwargs : <br>
    > 키워드를 함께 보낼 수 있다. <br> 
    > 딕셔너리 형태로 전달된다.

    ``` python
    alist = [[1,2,3], [4,5,6], [7,8,9]]
    for i in zip(*alist):
        print(i)
    
    # 출력
    #(1, 4, 7)
    #(2, 5, 8)
    #(3, 6, 9)
    ```

<br>

2. map
- map은 리스트의 요소를 지정된 함수로 처리해주는 함수
- map은 원본 리스트를 변경하지 않고 새로운 리스트를 생성

    ``` python 
    a = [1.2, 2.5, 3.7, 4.6]
    a = list(map(int, a))
    a

    # 출력
    # [1, 2, 3, 4]

    # 리스트뿐만 아니라 여러 반복 가능한 객체를 넣을 수 있음
    a = list(map(str, range(10)))
    a

    # 출력
    # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ```

<br>

3. defaultdict
- 딕셔너리에 접근할 때, 존재하지 않는 key에 대해 접근할 경우 keyError가 발생
- 따라서 반드시 key 값이 먼저 존재하는지 여부를 파악하고 없다면 초기화를 하여 에러 방지 필요

    ``` python 
    animals = ['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
    dic = {}
    
    for animal in animals:
        # key가 있다면 1 증가
        if animal in dic.keys():
            dic[animal] += 1
        # key가 없다면 1로 초기화
        else:
            dic[animal] = 1
    
    print(dic)
    ```

- defualtdict()의 매개변수로 int를 추가하여 초기값을 0으로 세팅

    ``` python 
    from collections import defaultdict

    animals = ['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
    dic = defaultdict(int)
    
    for animal in animals:
        dic[animal] += 1
    
    print(dic)
    print(dic['door'])
    print(dic)
    ```