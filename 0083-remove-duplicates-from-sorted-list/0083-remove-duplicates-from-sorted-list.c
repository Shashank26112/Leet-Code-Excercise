struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {
        return head; // Handle empty or single-node list
    }

    struct ListNode* current = head;
    struct ListNode* prev = NULL;

    while (current != NULL) {
        if (prev != NULL && current->val == prev->val) {
            // Duplicate found, remove current node
            prev->next = current->next;
            free(current);
            current = prev->next;
        } else {
            // No duplicate, move pointers
            prev = current;
            current = current->next;
        }
    }

    return head;
} 