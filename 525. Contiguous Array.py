
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

Solution__________________________________________
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum,dict,res=0,{},0
        for i in range(len(nums)):
            #adding -1 if element is 0 and 1 if its 1
            sum+=1 if nums[i]==1 else -1
            if sum==0 and res<i+1:
                res=i+1
            elif sum not in dict:
                #storing index as values
                dict[sum]=i
            elif sum in dict:
                #if the sum has already appeared before and appearing again
                #it means there has been equal addition n subtraction of 1's in between
                res=i-dict[sum] if res<(i-dict[sum]) else res
        return res
                
                
