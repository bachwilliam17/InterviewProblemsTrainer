# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        l3 = ListNode()
        res = l3

        carry = total = 0

        while l1 or l2 or carry : 
            total = carry

            if l1 : 
                total += l1.val
                l1 = l1.next
            if l2 : 
                total += l2.val
                l2 = l2.next

            new_number = total % 10
            carry = total // 10
            
            l3.next = ListNode(new_number)
            l3 = l3.next

        return res.next
