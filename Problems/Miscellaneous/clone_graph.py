### 133. MEDIUM
### STATUS: 
### BEATS
from util.node import Node
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return None
        # Dictionary for all nodes. Key = original. Value = cloned
        # Dont add neighbors now
        cloned = {node: Node(node.val)}
        # Keep a explore queue
        explore = deque()
        explore.append(node)
        explore.extend(node.neighbors)
        while explore:
            # Get current node
            current = explore.popleft()
            if current not in cloned:
                cloned[current] = Node(current.val)
                explore.extend(current.neighbors)
        # Add neighbors to each new node
        for original, new in cloned.items():
            new_neighbors = []
            for n in original.neighbors:
                new_neighbors.append(n)
            new.neighbors = new_neighbors
        return cloned[node]
    

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.setNeighbors([node2, node4])
node2.setNeighbors([node1, node3])
node3.setNeighbors([node2, node4])
node4.setNeighbors([node3, node1])
a = Solution()
a.cloneGraph(node1)