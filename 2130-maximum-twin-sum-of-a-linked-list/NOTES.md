​1. 예제를 따라하다가 코드의 결과가 다른 이유를 찾지 못해서 chatGPT에 질문

질문: 1) 과 2)의 결과가 다른 이유가 뭘까?

``` python 
1) middle.next, prev, middle = prev, middle, middle.next

2)
middle.next = prev
prev = middle
middle = middle.next
```



답변

```
첫 번째 코드 라인인 middle.next, prev, middle = prev, middle, middle.next은 튜플 언패킹을 사용하여 여러 변수에 값을 할당하는 작업입니다. 이때, 튜플의 값은 동시에 할당되는 것이 아니라 왼쪽에서 오른쪽으로 순차적으로 할당됩니다. 즉, middle.next가 prev로 할당되고, 그 다음 prev가 middle로 할당되며, 마지막으로 middle이 middle.next로 할당됩니다. 따라서 middle.next의 값은 첫 번째 코드 라인이 실행되기 이전의 middle.next 값이 됩니다.

반면 두 번째 코드 라인인 middle.next = prev; prev = middle; middle = middle.next은 연속적인 명령문으로, 변수들이 순차적으로 변경됩니다. middle.next 값이 먼저 prev로 업데이트되고, 그 다음에 prev가 middle로 업데이트되며, 마지막으로 middle이 middle.next로 업데이트됩니다. 이렇게 순차적으로 실행되기 때문에 middle.next의 값은 두 번째 코드 라인이 실행된 후의 값이 됩니다.
```