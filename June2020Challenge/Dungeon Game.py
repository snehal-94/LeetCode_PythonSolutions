The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. 
The dungeon consists of M x N rooms laid out in a 2D grid.
Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 
if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters 
and the bottom-right room where the princess is imprisoned.


Solution___________________________________________________________________

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r,c=len(dungeon),len(dungeon[0])
        dp=[[0]*c for i in range(r)]
        #bottom up approach
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                #we fill every positive cell with 0 to get the exact cost in terms of negative cell value
                if i==r-1 and j==c-1:  # if rightmost cell of last row 
                    dp[i][j]=min(0,dungeon[i][j])
                elif i==r-1: #last row
                    dp[i][j]=min(0,dp[i][j+1]+dungeon[i][j])
                elif j==c-1: #last column
                    dp[i][j]=min(0,dp[i+1][j]+dungeon[i][j])
                else: #choose the max cell value from right cell or the cell beneath,
                      #as max value means lower cost
                    dp[i][j]=min(0,dungeon[i][j]+max(dp[i+1][j],dp[i][j+1]))
        return abs(dp[0][0])+1



