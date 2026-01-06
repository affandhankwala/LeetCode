### 57. MEDIUM
### STATUS: SOLVED
### BEATS: 6.7%
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(newInterval) == 0: return intervals
        if len(intervals) == 0: return [newInterval]
        start, end = newInterval
        intersections = []
        i = 0
        while i < len(intervals):
            # Find intervals that intersect newInterval
            cur_int = intervals[i]
            cur_int_start, cur_int_end = cur_int
            if ((cur_int_start <= start and cur_int_end >= start) or
                (start <= cur_int_start and end >= cur_int_start)):
                # Determine how many other intervals intersect
                intersections.append(i)
                j = i + 1
                while j < len(intervals):
                    next_int = intervals[j]
                    next_int_start, next_int_end = next_int
                    if next_int_start <= end:
                        # Intersect
                        intersections.append(j)
                    j += 1
                break
            i += 1
        if len(intersections) == 0: 
            # No intersections, just insert and return
            for i, interval in enumerate(intervals):
                s, _ = interval
                if newInterval[0] < s:
                    intervals.insert(i, newInterval)
                    return intervals
            # Add to the end
            intervals.append(newInterval)
            return intervals
        # Intersections so need to combine
        first_interval_ind, last_interval_ind = intersections[0], intersections[len(intersections) - 1]
        
        starting_value = min(intervals[first_interval_ind][0], start)
        ending_value = max(intervals[last_interval_ind][1], end)
        intervals[first_interval_ind] = [starting_value, ending_value]
        # One interval intersection check
        if first_interval_ind == last_interval_ind:
            return intervals
        # Multiple intersection requires removing the extra intervals
        difference = last_interval_ind - first_interval_ind
        i = 0
        while i < difference:
            intervals.pop(first_interval_ind + 1)
            i += 1
        return intervals


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
a = Solution()
print(a.insert(intervals, newInterval))