# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: 
            return None
        # Use queue to track nodes per level
        queue = deque()
        queue.append(root)
        level_total, current_level = 0, 1
        highest_sum, highest_sum_level = -999999999, 1
        while queue:
            # Pop all from queue and keep track of sum. Order doesn't matter
            for i in range(len(queue)):
                popped_node = queue.popleft()
                if popped_node:
                    level_total += popped_node.val
                    # Transfer children if they are defined
                    if popped_node.left: queue.append(popped_node.left)
                    if popped_node.right: queue.append(popped_node.right)

            if level_total > highest_sum:
                highest_sum = level_total
                highest_sum_level = current_level
            level_total = 0
            # Swap queue, reset children, and increment level
            current_level += 1
        return highest_sum_level

        