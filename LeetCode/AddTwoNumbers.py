# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:


    def addTwoNumbers(self, l1, l2):
        # initializing current node to the head of returning result linked list
        result = ListNode(0)
        tmp = result
        carry = 0

        # while l1 and l2 can be none, carry can be 1
        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # definition of division
            carry, out = divmod(val1 + val2 + carry, 10)

            # setting the modular value to current node's next, and advancing current node
            tmp.next = ListNode(out)
            tmp = tmp.next

            # advancing l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # returning result's next (which is the dummy head)
        return result.next