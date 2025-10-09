# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        prev, cur = None, head

        while cur : 
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next

        return prev
    
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not head : return None

        newHead = head
        if head.next : 
            newHead = reverseList(head.next) # type: ignore
            head.next.next = head
        head.next = None

        return newHead
