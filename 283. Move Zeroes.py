Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.


Solution___________________________________________
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
#         for i in nums:
#             if i==0:  
#                 nums.append(nums.pop(nums.index(i)))
        i = 0
        for j in range(0, len(nums)):
            if(nums[j]!=0):
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                
                
        
