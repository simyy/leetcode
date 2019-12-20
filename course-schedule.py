# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/course-schedule/

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Analysis:
1. This is a topological sort problem.
2. Init a pre condition graph, key is a course, value is a list of pre condition.
3. Init a cache for record the course in path.
4. Loop every course:
    sub loop in the list of pre condition for the course
    check circle dependence exist or not
5. Using recursion to check sub course in the list of pre condition.
"""


class Solution(object):
    # store = set()
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # key: list()
        graph = {i: [] for i in range(numCourses)}
        # init a graph, records pre condition list
        for target, pre_condition in prerequisites:
            graph[target].append(pre_condition)

        # record reached course
        cached = {i: False for i in range(numCourses)}
        # loop for every course
        for course in range(numCourses):
            # check exist circle dependence
            # if one course exist circle dependence, return False
            if self.existCircleDFS(course, cached, graph):
                return False
        return True

    def existCircleDFS(self, course, cached, graph):
        # if cached course, exist circle dependence
        if cached[course]:
            return True
        # cached course
        cached[course] = True
        # loop the pre condition list of course
        # only every pre condition not exist cicle
        for pre_condition in graph[course]:
            # recursion every pre condition
            if self.existCircleDFS(pre_condition, cached, graph):
                return True
        # remove cached
        cached[course] = False
        return False

if __name__ == '__main__':
    s = Solution()
    #print s.canFinish(2, [[1, 0], [0, 1]])
    #print s.canFinish(1, [])
    #print s.canFinish(2, [[1, 0]])
    print(s.canFinish(100, [[6,27],[83,9],[10,95],[48,67],[5,71],[18,72],[7,10],[92,4],[68,84],[6,41],[82,41],
                            [18,54],[0,2],[1,2],[8,65],[47,85],[39,51],[13,78],[77,50],[70,56],[5,61],[26,56],
                            [18,19],[35,49],[79,53],[40,22],[8,19],[60,56],[48,50],[20,70],[35,12],[99,85],[12,75],
                            [2,36],[36,22],[21,15],[98,1],[34,94],[25,41],[65,17],[1,56],[43,96],[74,57],[19,62],[62,78],
                            [50,86],[46,22],[10,13],[47,18],[20,66],[83,66],[51,47],[23,66],[87,42],[25,81],[60,81],[25,93],
                            [35,89],[65,92],[87,39],[12,43],[75,73],[28,96],[47,55],[18,11],[29,58],[78,61],[62,75],[60,77],
                            [13,46],[97,92],[4,64],[91,47],[58,66],[72,74],[28,17],[29,98],[53,66],[37,5],[38,12],[44,98],
                            [24,31],[68,23],[86,52],[79,49],[32,25],[90,18],[16,57],[60,74],[81,73],[26,10],[54,26],[57,58],
                            [46,47],[66,54],[52,25],[62,91],[6,72],[81,72],[50,35],[59,87],[21,3],[4,92],[70,12],[48,4],[9,23]]));

