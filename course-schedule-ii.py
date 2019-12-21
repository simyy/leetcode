# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/course-schedule-ii/

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites,
for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders,
you just need to return one of them.
If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

Analysis:
1. This is a topological sort problem.
2. All directed graph can use indegree and nextGraph to solve it.
3. Indegree is the in-degree for directed graph, which records the number of it depened on.
4. NextGraph record the next multi node that current node point to.
5. Use a queue to record which indegree is zero, that means the node in queue is not depend on any other node out of queue.
6. First : find the node which indegree is zero
7. Second: loop every node in queue, find the next node of node in queue,
            and move the node to queue which not depend on the node out of queue.
8. If loop is end, check the number of node is right or not.
"""

from Queue import Queue


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Init indegree for course
        indegree = {i: 0 for i in range(numCourses)}
        # Init a graph to record course  which depend on
        graph = {i: [] for i in range(numCourses)}
        for p, pre in prerequisites:
            indegree[p] += 1
            graph[pre].append(p)

        # Init a queue to record course in path
        queue = Queue(numCourses)
        # Put course to queue that the indegree of course is 0
        # indegree == 0 means it not depend on any course
        for i in indegree:
            if indegree[i] == 0:
                queue.put(i)

        # Init result to record course in path
        result = []

        # Start loop from queue
        # The course in Queue is only depend on its self
        while not queue.empty():
            # Select one course in queue
            p = queue.get()
            # Put queue to result
            result.append(p)
            # Get the next course list of  course P
            nextList = graph[p]
            # Traverse every next course for course P
            for nextOne in nextList:
                # indegree - 1
                indegree[nextOne] -= 1
                # If indegree of current course is 0, then it not depend on any course in out of queue
                if indegree[nextOne] == 0:
                    queue.put(nextOne)

        return result if len(result) == numCourses else []


if __name__ == '__main__':
    s = Solution()
    rs1 = s.findOrder(3, [[1, 0], [2, 0]])
    #rs1 = s.findOrder(3, [[1, 0]])
    print '===> rs1', rs1
    # rs2 = s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    # print '===> rs2', rs2