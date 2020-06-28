Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Solutions______________________________________________________________

class Solution:
    def numSquares(self, n: int) -> int:
        # Recursion+ Memoization
        mem=[-1]*(n+1)
        def solve(n):
            if n<=3:return n
            if mem[n]!=-1: return mem[n]
            i,ans=1,n
            #As 1 is a perfect square , worst case of perfect squares to make n could be n only.
            #Hence ans is initialized to n.
            while i*i<=n:
                ans=min(ans,1+solve(n-i*i))
                i+=1
            mem[n]=ans
            return ans
        ans=solve(n)
        return ans 
        
        #Dynamic Programing
        if n<=3: return n
        dp=[0]*(n+1)  
        for i in range(1,n+1):
            dp[i]=i
            j=1
            while(j*j<=i):
                dp[i]=min(dp[i],1+dp[i-j*j])
                j+=1
        return dp[n]
