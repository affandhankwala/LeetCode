### 104. EASY
### STATUS: SOLVED
### BEATS: 100%
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.depthRecursive(root, 0)
        
    def depthRecursive(self, node, depth):
        if not node:
            return depth
        # Increase depth
        depth += 1
        # Return the maximum of the children
        return max(
            self.depthRecursive(node.left, depth),
            self.depthRecursive(node.right, depth)
        )