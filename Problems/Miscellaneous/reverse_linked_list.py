### 206 EASY
### STATUS: SOLVED
### BEATS: 100%
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        prev_node, cur_node, next_node = None, head, head

        while next_node is not None:
            cur_node = next_node
            next_node = next_node.next
            cur_node.next = prev_node
            prev_node = cur_node
        return prev_node
        