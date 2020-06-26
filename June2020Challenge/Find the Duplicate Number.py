Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

Solution_________________________________________________________________

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    
        #Brute Force...very slow....
        for i in range(len(nums)):
            if nums[i] in nums[:i] or nums[i] in nums[i+1:]: return nums[i]
   _________________________________________________________________________
   
        #Using Counter
        
        return sorted(Counter(nums).items(), key=lambda x: x[1])[-1][0]
        
  __________________________________________________________________________
  
         #Floyd's tortoise and hare method
        t,h=nums[0],nums[nums[0]]
        while t!=h: t,h=nums[t],nums[nums[h]]
        t=0
        while t!=h: t,h=nums[t],nums[h]
        return t
   ________________________________________________________________________
    #Applicable only on arrays having positive numbers
    #take the abs values for each index and treat them as index 
        #and change the value for that index to negative. If we find the value is already negative that 
        #means it was visited before
        for i in range(len(nums)):
            val=nums[i]
            if nums[abs(val)]<0: return abs(val)
            else: nums[abs(val)]=-nums[abs(val)]
