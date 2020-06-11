Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

Solution______________________________________________________

from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Two Pass
        
        n=[0]*3
        #storing the count in a different list n. only 0,1,2 are the nums, hence
        for i in nums:
            n[i]+=1
        for i in range(len(nums)):
            if i<n[0]: nums[i]=0
            elif i<n[0]+n[1]: nums[i]=1
            else: nums[i]=2
        
        ______________________________________________________
        
        #One pass (3 pointers-Dutch flag problem)
        
        i,low,high=0,0,len(nums)-1
        while i<=high:
            if nums[i]==0:
                nums[low],nums[i]=nums[i],nums[low]
                i+=1
                low+=1
            elif nums[i]==2:
                nums[high],nums[i]=nums[i],nums[high]
                high-=1
            else: i+=1
        
