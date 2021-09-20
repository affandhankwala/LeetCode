//Given a sorted Linked List, remove all duplicates from it


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
    public ListNode deleteDuplicates(ListNode head) {
        //Start at head
        //Have variable representing current value
        //Start traversal
        //If see another node with same val as stored value, delete it
        //Delete by routing parent and current ptr pointers
        //If next node value is different, assign that val to value
        //Terminate when current ptr is null
        
        ListNode ptr = head;
        ListNode parent = null;
        int currentVal = -101; //Lowest value is -100
        
        while(ptr != null){
            //Check if we need to change value of currentVal
            if(currentVal != ptr.val){
                currentVal = ptr.val;
                parent = ptr;
            }
            else{
                //Parent SHOULD NOT be null
                //But we will safeguard either way
                if(parent == null){
                    head = ptr.next;
                }
                else{
                    parent.next = ptr.next;
                }
            }
            ptr = ptr.next;
        }
        return head;
    }
}
