# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# from parseBoolExpr.parseBool import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        return addTwoHelper(l1, l2)


def addTwoHelper(l1: Optional[ListNode], l2: Optional[ListNode]):
    carry: int = 0

    last_node: ListNode = None
    first_node: ListNode = None

    while (l1 != None and l2 != None):

        accumulator = l1.val + l2.val + carry
        carry = get_carry(accumulator)
        last_dig = accumulator % 10

        new_node = ListNode(last_dig, None)

        if last_node != None:
            last_node.next = new_node
        else:
            first_node = new_node
        last_node = new_node

        PRINTS_ACTIVE = True
        if PRINTS_ACTIVE:

            print(f'accumulator = {accumulator}\tcarry = {
                  carry}\tlast_dig = {last_dig}')
            print(f'last_node val = {last_node.val}')

        l1 = l1.next
        l2 = l2.next

    while (l1 != None):
        accumulator = l1.val + carry
        carry = get_carry(accumulator)
        last_dig = accumulator % 10
        new_node = ListNode(last_dig, None)
        if last_node != None:
            last_node.next = new_node
        else:
            first_node = new_node
        last_node = new_node
        l1 = l1.next

    while (l2 != None):
        accumulator = l2.val + carry
        carry = get_carry(accumulator)
        last_dig = accumulator % 10
        new_node = ListNode(last_dig, None)
        if last_node != None:
            last_node.next = new_node
        else:
            first_node = new_node
        last_node = new_node
        l2 = l2.next
    if carry > 0:

        accumulator = carry
        last_dig = carry % 10
        new_node = ListNode(last_dig, None)
        last_node.next = new_node
        last_node = new_node

    if PRINTS_ACTIVE:
        print(f'first node = {first_node}')

    return first_node


def get_carry(i: int) -> int:
    return 1 if (i >= 10) else 0
