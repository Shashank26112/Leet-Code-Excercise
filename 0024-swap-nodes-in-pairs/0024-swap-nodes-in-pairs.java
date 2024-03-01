class Solution {
    public ListNode swapPairs(ListNode head) {
         if(head==null){
            return null;
        }
        ListNode dummy=new ListNode(-1);
        dummy.next=head;
        ListNode cur=dummy;

        while(cur.next!=null && cur.next.next!=null){
            ListNode first=cur.next;
            ListNode sec=cur.next.next;

            first.next=sec.next;
            sec.next=first;
            cur.next=sec;

            //make current point to first pointer
            cur=first;
        }
        return dummy.next;
    }
}
