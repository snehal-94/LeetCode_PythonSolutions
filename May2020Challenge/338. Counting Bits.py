Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.



Solution 1________________________________________

class Solution:
    def countBits(self, num: int) -> List[int]:
        f=lambda i: str(bin(i)).count('1')
        res=[f(i) for i in range(0,num+1)]
        return res
        
Solution 2_________________________________________

class Solution:
    def countBits(self, num: int) -> List[int]:
        res=[str(bin(i)).count('1') for i in range(0,num+1)]
        return res
        
Solution 3_________________________________________

class Solution:
    def countBits(self, num: int) -> List[int]:
        # f=lambda i: str(bin(i)).count('1')
        # res=[f(i) for i in range(0,num+1)]
        # return res
        return [f'{i:030b}'.count('1') for i in range(0,num+1)]
        
