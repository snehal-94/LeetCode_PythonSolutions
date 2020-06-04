Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

Solution
________________________________________________
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        a=Counter(s1)
        b=Counter(s2[:len(s1)])
        i=len(s1)
        pos=0
        while i<=len(s2):
            if a==b:
                return True
            b[s2[pos]]-=1
            if b[s2[pos]]<=0:
                b.pop(s2[pos])
            if i<len(s2):
                b[s2[i]]+=1
            i+=1
            pos+=1
        return False

        
