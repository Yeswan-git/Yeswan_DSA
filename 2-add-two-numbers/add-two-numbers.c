/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode dummy;
    struct ListNode* current = &dummy;
    
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry > 0) {
        int sum = (l1 != NULL ? l1->val : 0) + 
                  (l2 != NULL ? l2->val : 0) + 
                  carry;

        int digit = sum % 10;
        carry = sum / 10;

        struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = digit;
        newNode->next = NULL;

        current->next = newNode;
        current = current->next;

        if (l1 != NULL) l1 = l1->next;
        if (l2 != NULL) l2 = l2->next;
    }

    // The actual result starts after the dummy node
    return dummy.next;
}