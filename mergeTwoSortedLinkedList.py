"""
Create a dummy node as a placeholder to simplify pointer handling.
Use a pointer tail that always refers to the end of the merged list.
While both lists are not empty:
Compare the current values of list1 and list2.
Attach the node with the smaller value to tail.next.
Move forward in the list from which the node was taken.
Update tail to the newly attached node.
When one list is exhausted, connect the remaining part of the other list to the merged result.
Return dummy.next as the head of the new merged list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        tail = dummy

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1 != None:
            tail.next = list1
        if list2 != None:
            tail.next = list2

        return dummy.next
