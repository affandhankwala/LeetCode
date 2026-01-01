//Merge two sorted linked lists into one large sorted Linked List and return it. 

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode first = new ListNode (0);
        ListNode last = first;
        while(true){
            if(l1 == null){
                last.next = l2;
                break;
            }
            else if(l2 == null){
                last.next = l1;
                break;
            }
            else if(l1.val < l2.val){
                last.next = l1;
                l1 = l1.next;
            }
            else{
                last.next = l2;
                l2 = l2.next;
            }
        last = last.next;
        }
        return first.next;
    }
    
}
