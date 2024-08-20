//   Definition for singly-linked list.
#include <stdio.h>
#include <stdlib.h>
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *num_to_lnode(u_int64_t input_num)
{

    struct ListNode *prev = NULL;
    // struct ListNode* curr = NULL;
    while (input_num > 0)
    {
        u_int8_t last_digit = input_num % 10;
        input_num /= 10;
        struct ListNode *internal_curr = (struct ListNode *)malloc(sizeof(struct ListNode));
        internal_curr->val = last_digit;
        internal_curr->next = prev;
        prev = internal_curr;
    }

    return prev;
}
struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    struct ListNode *l1_ptr = l1;
    u_int64_t l1_num = 0;
    u_int8_t l1_len = 0;
    while (l1_ptr != NULL)
    {
        l1_len++;
        l1_num += l1_ptr->val;
        l1_ptr = l1_ptr->next;
    }

    struct ListNode *l2_ptr = l1;
    u_int64_t l2_num = 0;
    u_int8_t l2_len = 0;
    while (l2_ptr != NULL)
    {
        l2_len++;
        l2_num += l2_ptr->val;
        l2_ptr = l2_ptr->next;
    }

    for (; l1_len < l2_len; l1_len++)
    {
        l1_num *= 10;
    }
    for (; l2_len < l1_len; l2_len++)
    {
        l2_num *= 10;
    }

    u_int64_t resulting_num = l1_num + l2_num;

    num_to_lnode(resulting_num);
}
