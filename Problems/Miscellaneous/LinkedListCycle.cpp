/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        //Make 2 pointers traverse this linked list
        //One of them moves by 1 and the other moves by 2
        //If the fast one turns out to be null then we know there is no cycle
        //If both point to same node then there is cycle
        ListNode slow = head;
        ListNode fast = head;
        while(fast!=null && fast.next != null){
            //Increment slow
            slow = slow.next;
            //Check if slow is valid and if so then increment fast by 2;
            if(slow!=null) fast = fast.next.next;
            //If slow not valid (only one node) then no cycle and return false
            else return false;
            
            if(slow == fast) return true;
            //If both are equal to one another then there is cycle
            
        }
        //If fast becoems null then there is no cycle
        return false;
    }
}
