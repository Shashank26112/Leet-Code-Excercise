class Solution:
    def swapNodes(self, head, k):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        n = count - k + 1
        begin = None
        end = None
        count = 0
        curr = head
        while curr:
            count += 1
            if count == k:
                begin = curr
            if count == n:
                end = curr
            if end is not None and begin is not None:
                break
            curr = curr.next
        begin.val, end.val = end.val, begin.val
        return head

