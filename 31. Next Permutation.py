'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''

Solution:
_________________________________________________________

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        id=len(nums)-2
        while id>=0:
            if nums[id]<nums[id+1]:
                break
            id-=1
        if id<0:
            nums.sort()
            return
        
        nextId=id+1
        
        while nextId<len(nums) and nums[nextId]>nums[id]:
            nextId+=1
        
        #swap id and nextid
        nums[nextId-1],nums[id]=nums[id],nums[nextId-1]
        
        #sorting the remaining string to the right
        nums[id+1:]=nums[id+1:][::-1]
        
        
