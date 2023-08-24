# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not head.next:
    	    return head.next

        fast, slow = head.next.next, head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
        slow.next = slow.next.next
        return head
        
        
        # list를 = 로 대입하는 것은 얕은 복사이기 때문에
        # slow와 fast를 나누어서 중간에 연결을 끊어버리면 노드 삭제가 된다.
            

            
            
        
         
            