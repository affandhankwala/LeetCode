//Remove all nodes in LinkedList with same value as passed in parameter

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
    public ListNode removeElements(ListNode head, int val) {
        ListNode ptr = head;
        ListNode parent = null;
        while(ptr != null){
            //Compare value of ptr with target
            if(ptr.val != val){
                parent = ptr;
                ptr = ptr.next;
            }
            else{
                //Check if parent pointer is valid
                if(parent != null){
                    //This means we have to link the parent to the next node
                    parent.next = ptr.next;
                }
                else{
                    //No parent means the target node is head node
                    head = ptr.next;
                }
                ptr = ptr.next;
           }
        }
                return head;
    }
}
