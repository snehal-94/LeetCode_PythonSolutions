Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

Solution___________________________________________________________________

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums: return nums.index(target)
        l,h=0,len(nums)-1
        while l<=h:
            m=l+(h-l)//2
            if nums[m]>target:h=m-1
            else: l=m+1
        return l
        
        
