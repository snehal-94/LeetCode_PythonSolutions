Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1

Solution
___________________________________________________

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        while(i**2<=num):
            if((num%i==0) and (num/i==i)):
                return True
            i+=1
        return False
        
