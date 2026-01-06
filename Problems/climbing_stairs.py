### 70. EASY
### Status: SOLVED

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        if n == 1: return 1

        p1, p2 = 1, 1
        for i in range(2, n + 1):
            current = p1 + p2
            p1 = p2
            p2 = current
        return p2
num = 2
a = Solution()
print(a.climbStairs(num))