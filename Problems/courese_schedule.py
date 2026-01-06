###207. MEDIUM
### STATUS: SOLVED
### BEATS: 10.57%
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # Set up dictionary for all courses
        # Populate dictionary with all empty prerequisites
        courses = {i: [] for i in range(0, numCourses)}
        # Map all courses (key) to their prerequisites (values)
        for p in prerequisites:
            course, prereq = p
            courses[course].append(prereq)

        # Recursively check each element
        for key in courses.keys():
            if not self.prereqsOk(courses, key, []):
                return False
        return True
    
    def prereqsOk(self, courses, course, visited):
        # If courses[course] is [], return
        if courses[course] == []:
            return True
        # Else, check if we have already hit this course
        if course in visited:
            return False
        visited.append(course)
        # Iterate through prereqs of this course
        for prereq in courses[course]:
            if not self.prereqsOk(courses, prereq, visited):
                # Not possible, terminate
                return False
        # Valid so set prereq list to [] and remove from visited
        visited.remove(course)
        courses[course] = []
        return True
    
prerequisites = [[1,0]]
numCourses = 2
a = Solution()
print(a.canFinish(numCourses, prerequisites))