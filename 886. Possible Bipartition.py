
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Constraints:

1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].


Solution__________________________________________

import collections
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        edges=collections.defaultdict(list)
        for u,v in dislikes:
            edges[u].append(v)
            edges[v].append(u)
        seen=set()
        #colors dictionary stores colors for each of N elements
        colors={}
        
        def rec(p,color):
            seen.add(p)
            #if the element is already in colors with a different color 
            #than the one it should have, return False
            if p in colors:
                return colors[p]==color
            #assigning one of the 2 colors, 0/1
            colors[p]=color
            flag=True
            for i in edges[p]:
                if i not in seen:
                    #adding the connections of p in the seen if not present
                    #passing alternate color for all connections.%2 produces either 0 or 1
                    flag &=rec(i,(color+1)%2)
                if colors[p]==colors[i]:
                    return False
            return flag
        
        for p in range(1,N+1):
            if p not in seen:
            #calling with initial color as 0
                if not rec(p,0):
                    return False
        return True
