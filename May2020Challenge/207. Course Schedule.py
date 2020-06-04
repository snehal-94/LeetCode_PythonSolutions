There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5


Solution______________________________________________

import collections
class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        edges=collections.defaultdict(list)
        for u,v in prereq:
            edges[u].append(v)
        visited=[0]*numCourses
        
        def cyclePresent(edges,visited,i):
            if visited[i]==2:
                return True
            visited[i]=2
            for x in edges[i]:
                if visited[x]!=1:
                    if cyclePresent(edges,visited,x):
                        return True
            visited[i]=1
            return False   
        
        for i in range(numCourses):
            if visited[i]==0:
                if cyclePresent(edges,visited,i):
                    return False
        return True
