# class Solution:
#     def climbStairs(self, n: int) -> int:
#         ago_2 = 1
#         ago_1 = 2
#         curr = 2 if n == 2 else 1
#         for _ in range(2, n):
#             curr = ago_2 + ago_1
#             ago_2 = ago_1
#             ago_1 = curr

#         return curr
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = head
        next = head.next
        prev.next = None
        while next != None:
            print(f'head = {head.val}, next = {next.val}')

            next_next = next.next
            next.next = prev
            prev = next
            next = next_next
        return prev
