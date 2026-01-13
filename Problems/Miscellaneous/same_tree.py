### 100. EASY
### STATUS: SOLVED
### BEATS: 100%
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        return self.isSameTreeHelper(p, q)
    
    def isSameTreeHelper(self, node1, node2): 
        # Check if null 
        if not node1: 
            # If node 2 is defined, then return false
            if node2: 
                return False
            return True
        elif not node2: 
            # Node 1 is not null
            return False

        # Compare the two values
        if node1.val != node2.val: 
            return False

        # Check children
        left_same = self.isSameTreeHelper(node1.left, node2.left)
        right_same = self.isSameTreeHelper(node1.right, node2.right)
        # Return validity
        if not left_same or not right_same:
            return False
        return True