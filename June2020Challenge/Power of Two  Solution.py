Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

Solution_______________________________________________________________

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #1st Solution
        x=0
        while(pow(2,x)<=n):
            if n==pow(2,x):
                return True
            x+=1
        return False
  __________________________________________________________________________      
        #2nd Solution
        if n<=0:return False
        while n>=1:
            if n==1: return True
            elif n%2==0: n=n/2
            else: return False
        return True
  ________________________________________________________________________      
        # 3rd Solution
        #int has range of -2**31 to 2**31.Hence n should be completely divisible by 2**31
        if n is a multiple of 2
        return n>0 and 2**31%n==0
    _____________________________________________________________________
        #4th Solution
        #Bit manipulation
        #All no.s divisible by 2 will have only one 1 in their binary representation.
        #Hence the rightmost 1 in the binary version would be the only one 1 present.
        #if we flip it, it becomes 0.
        if n<=0: return False
        return n&(n-1)==0
