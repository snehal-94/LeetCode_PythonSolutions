'''
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
num >= 1
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
'''

Solution:
________________________________________________

class Solution:
    def findComplement(self, num: int) -> int:
        i=num
        binStr=''
        complementStr=''
        finalNum=0
        while i>0:
            modVal=i%2
            binStr+=str(modVal)
            i=i//2
        binStr=binStr[::-1]
        binStr=binStr.lstrip("0")
        for i in range(len(binStr)):
            if (binStr[i]==str(1)):
                complementStr+=str(0)
            elif (binStr[i]==str(0)):
                complementStr+=str(1)
        lengthC=len(complementStr)-1
        
        for i in range(len(complementStr)):
            finalNum+=(2**lengthC)*int(complementStr[i])
            lengthC-=1
        return finalNum
            
        
