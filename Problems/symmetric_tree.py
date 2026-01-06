### 101. EASY
### STATUS: SOLVED
### BEATS: 100%
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root: 
            return True
        return self.isSymmetricRecursive(root.left, root.right)
    
    def isSymmetricRecursive(self, left, right):
        if not left:
            if not right:
                # Symmetric
                return True
            # Not symmetric
            else:
                return False
        if not right:
            # Not symmetric
            return False
        # Compare values
        if left.val != right.val:
            return False
        # See if the left child of left == right child of right (outside pair)
        outside_same = self.isSymmetricRecursive(left.left, right.right)
        # See if the right child of left == left child or right (inside pair)
        inside_same = self.isSymmetricRecursive(left.right, right.left)

        # If both are True, it is symmetric
        if outside_same and inside_same:
            return True
        else:
            return False