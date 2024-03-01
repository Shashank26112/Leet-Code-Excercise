class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def sortedListToBST(self, head):
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        self.head = head
        
        def rec(st, end):
            if st > end:
                return None
            mid = (st + end) // 2
            left = rec(st, mid - 1)          
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left
            root.right = rec(mid + 1, end)
            return root
        return rec(0, n - 1)