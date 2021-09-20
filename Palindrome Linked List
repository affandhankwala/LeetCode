//Checks if a linked List is a palindrome


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
    public boolean isPalindrome(ListNode head) {
        //Loop through entire linked list and count all the nodes
        //Create array with same size as linked list
        //Go through array again and transfer each value into array
        //Validate array is palindrome
        // **Code**
        
        //Size of linked list
        int size = 0;
        ListNode temp = head;
        while(temp != null){
            temp = temp.next;
            size++;
        }
        
        //Now size is size of array
        int[] arr = new int[size];
        
        //Reset temp pointer
        temp = head;
        //Transfer each value of linkedlist to array
        for(int i = 0; i < size; i++){
            arr[i] = temp.val;
            temp = temp.next;
        }
        
        //Validate array is palindrome
        for(int i = 0; i < arr.length/2; i++){
            if(arr[i] != arr[arr.length - i - 1]) return false;
        }
        return true;
        
    }
}
