'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
 

Note: You may assume the string contain only lowercase English letters.
'''

Solution:
________________________________________________

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=[0]*256
        index=-1
        x=0
        for i in s:
            count[ord(i)]+=1
        for l in s:
            if (count[ord(l)]==1):
                index=x
                break
            x+=1
        return index
        
