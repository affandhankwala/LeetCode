//Finds the middle node of a linked list
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
    public ListNode middleNode(ListNode head) {
        //Have 2 pointers
        //First one traverses entire list and counts total number of nodes
        //After finding total number of nodes, we perform Math.ceil (total / 2) 
        //This will either give us the middle or the first middle of the linked list (we need second)
        //Then we perform .next on first pointer (still at head) for that number of times and it will end up at middle node or second middle node
        //Return first pointer
        ListNode end = head;
        int size = 0;
        while (end != null){
            end = end.next;
            size++;
        }
        //At this point end is null 
        //Size is total number of nodes
        
        //Make middle go to next node through Math.ceil(size/2)
        ListNode middle = head;
        for(int i = 0; i < Math.ceil(size/2); i ++){
            middle = middle.next;
        }
        return middle;
    }
}
