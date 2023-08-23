# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next == None: return head
        
        tmp_res = ListNode(head.val) 
        tmp_store = head.next 
        while tmp_store.next != None:
            cur_node = tmp_store.val 
            tmp_store = tmp_store.next 
            
            tmp = ListNode(cur_node)
            tmp.next = tmp_res
            tmp_res = tmp
            
        tmp = ListNode(tmp_store.val)
        tmp.next = tmp_res
        tmp_res = tmp
            
        return tmp_res
            
