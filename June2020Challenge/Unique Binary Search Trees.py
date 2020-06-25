Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
Solution________________________________________________________________

class Solution:
    def numTrees(self, n: int) -> int:
        def catalan_no(n):
            dp=[0]*(n+1)
            dp[0]=dp[1]=1 # if n is 0 or 1, only 1 unique tree is possible
        #from n=2 to real n value we find unique trees and tht keeps adding up
            for i in range(2,n+1):
                #for each n,the root would be shifted to form different binary trees 
                #using elements in the left and right subtree
                #For ex: n=3, no of elements on the left-right subtree could be 0,2 or 1,1 or 2,0
                #as 1 node would be root. all of left nodes would be multiplied with all of 
                #right nodes
                for j in range(i):
                    dp[i]+=dp[j]*dp[i-j-1]
            return dp[-1]
        return catalan_no(n)
            
