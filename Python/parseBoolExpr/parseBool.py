from enum import Enum
from typing import List, Optional


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        ...


begOfExpr = '|', '&'
internal_exp_start = '('
internal_exp_end = ')'

and_start = '&('
or_start = '|('


class Token(Enum):
    OPEN_PAREN = 1,
    CLOSE_PAREN = 2,
    AND = 3
    OR = 4
    AND_START = 5
    OR_START = 6
# best to do this one via recursive descent most likely

# def getNextExpr(expr: str, start_pos: int) -> (str, int):
#     offsetFromStart = 0
#     num_starts_seen = 0
#     num_ends_seen = 0
#     for character in str[start_pos:]:
#         if character in begOfExpr:


def tokenize_input(expr: str) -> List[Token]:
    for (idx, character) in enumerate(expr):
        ...

# def is_expression_start(expr: str, start_pos: int):
#     if str[start_pos] in begOfExpr and str[internal_exp_start]:

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resulting_list_start: Optional[ListNode] = None
        resulting_list_end: Optional[ListNode] = None
        resulting_list_start: ListNode = 
        print(f'List1 = {list1}\tList2 = {list2}')
        while list1 != None and list1 != None:
            print(f'List1Val = {list1.val}\tList2Val = {list2.val}')
            if list1.val < list2.val:
                resulting_list_end = list1
                list1 = list1.next
            else:
                resulting_list_end = list2
                list2 = list2.next

            if resulting_list_start == None:
                resulting_list_start = resulting_list_end

        if resulting_list_start == None:

            if list1 != None:
                resulting_list_start = list1
            elif list2 != None:
                resulting_list_start = list2
        else:

            while list1 != None:
                resulting_list_start = list1
                list1 = list1.next

            while list2 != None:
                resulting_list_start = list2
                list2 = list2.next

        return resulting_list_start
