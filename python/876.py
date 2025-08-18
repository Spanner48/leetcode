# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        listLen = 0

        while head != None:
            arr.append(head)
            head = head.next
            listLen += 1

        return arr[listLen // 2]
