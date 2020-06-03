Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Solution
________________________________________________

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams=[]
        dict={}
        if len(p)>len(s):
            return []
        P=Counter(p)
        S=Counter(s[:len(p)])
        pos=0
        j=len(p)
        
        while j<=len(s):
            if P==S:
                anagrams.append(pos)
            S[s[pos]]-=1
            if S[s[pos]]<=0:
                S.pop(s[pos])
            if j<len(s):
                S[s[j]]+=1
            pos+=1
            j+=1
        return anagrams
                
