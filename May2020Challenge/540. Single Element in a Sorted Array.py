You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5

Solution__________________________________________________________________

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        L,R=0,len(nums)-1
        while L<R:
            m=L+(R-L)//2
            if m%2==1 and nums[m]==nums[m-1]: L=m+1
            #Since array index starts at 0, even mid means odd in reality
            elif m%2==0 and nums[m]==nums[m+1]: L=m+2
            else:R=m
        return nums[L]

