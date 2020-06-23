
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

Solution__________________________________________________________________

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #1st approach brute force
        rev=nums[::-1]
        le=len(nums)-1
        for i in nums:
            if nums.index(i)==le-rev.index(i):
                return i
 _________________________________________________________________________       
        # 2nd Approach using set takes extra space
        return (sum(set(nums))*3-sum(nums))//2
 _________________________________________________________________________        
        # 3rd approach using sorting + inear traversal O(logn+N)
        nums.sort()
        if len(nums)==1 or nums[0]!=nums[1]: return nums[0]
        if nums[-1]!=nums[len(nums)-2]: return nums[-1]
        i=1
        while i<len(nums)-2:
            if nums[i]==nums[i-1]: i+=3
            else: return nums[i-1]
