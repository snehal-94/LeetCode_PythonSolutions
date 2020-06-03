'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

Solution 1:
___________________________________________________

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newStr=''
        for i in digits:
            newStr+=str(i)
        newStr=int(newStr)
        newStr+=1
        newStr=str(newStr)
        output=[0]*len(newStr)
        for i in range(len(newStr)):
            output[i]=newStr[i]
        return output
 
 
 Solution 2:
 ____________________________________________________
 class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output=[] 
        for i in str(int(''.join(map(str,digits)))+1):
            output+=i #adding string elements to list
        return output
