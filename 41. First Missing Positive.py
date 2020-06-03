'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''

Solution:
________________________________________________

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l=len(nums)
        nums.sort()
        a=[x for x in nums if x > 0]
        if 1 not in a:
            return 1
        for i in nums:
            if (i>0):
                if (i+1) not in nums:
                    return i+1
