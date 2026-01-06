### 19. MEDIUM
### STATUS: DONE
### BEATS: 100%

from util.listnode import print_linked_list, convert_arr_to_linked_list
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        counter = 0        
        slow = fast = head
        new_list = new_list_head = None
        # Get fast n ahead of slow
        while counter < n:
            if fast:
                fast = fast.next
                counter += 1
            else:
                return head
        # Increment both at same rate
        # Increment slow_prev to always be 1 behind slow
        while fast:
            fast = fast.next
            slow = slow.next
            if not new_list_head:
                new_list = new_list_head = head
            else: 
                new_list = new_list.next
        # Remove element at slow
        if slow == head and n == 1:
            return None
        if not new_list_head:
            new_list_head = slow.next
        else:
            new_list.next = slow.next
        return new_list_head
    
arr = [1, 2, 3, 4, 5]
n = 2
head = convert_arr_to_linked_list(arr)
a = Solution()
print_linked_list(a.removeNthFromEnd(head, n))