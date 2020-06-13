Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]

Solution_________________________________________________________________

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)<=1: return nums
        #sort the array to get. 
        #The divisor should always be to the left in this way to fulfill the condition
        # Mod operationis expensive so instead of 2 times mod, one sort before and then 
        #comparing using mod is more efficient
        nums=sorted(nums)
        #Fill dp table with 1 since all no.s are divisible by themselves
        dp=[1]*len(nums)
        m=1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
                        if m<dp[i]: m=dp[i]
        #start from last element of dp and compare with max.
        #Push the subset accordingly
        x=len(nums)-1
        res,prev=[],-1
        while x>=0:
            if (dp[x]==m and (prev%nums[x]==0 or prev==-1)):          
                res.append(nums[x])
                m-=1
                prev=nums[x]
            x-=1
        return res
                
        
        
        
