class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        min_time = 0
        if len(points) < 2: return min_time

        i, j = 0, 1
        while j < len(points):
            p1, p2 = points[i], points[j]
            difference = [abs(p2[0] - p1[0]), abs(p2[1] - p1[1])]
            min_time += min(difference)
            for d in difference:
                d -= min(difference)
                min_time += d
            i += 1
            j += 1
        return min_time
        