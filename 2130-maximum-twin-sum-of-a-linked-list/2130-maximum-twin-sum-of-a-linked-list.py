# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # 중간 찾기
        
        middle, tail = head, head
        
        while tail and tail.next:
            middle = middle.next
            tail = tail.next.next

        
        # 오른쪽 리스트 reverse
        prev = None
        while middle:
            next_node = middle.next
            middle.next = prev
            prev = middle
            middle = next_node
            
            #middle.next, prev, middle = prev, middle, middle.next  # 한 줄로 나타낼때와 여러줄로 나타낼 때 결과가 다르다.

        max_val=0
        # max 값을 찾으러 가자
        while prev:
            max_val = max(max_val, head.val+prev.val)
            head = head.next
            prev = prev.next

        return max_val