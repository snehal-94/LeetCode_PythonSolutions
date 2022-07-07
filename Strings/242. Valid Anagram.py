Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


_________________________________________________________________________________________________________________________

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]]=1
            else:
                dict1[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in dict1:
                return False
            dict1[t[i]]-=1
            if dict1[t[i]]==0:
                dict1.pop(t[i])
        return not dict1
        
#         Another approach one liner
        if sorted(s)==sorted(t):
            return True
        return False
        
#         Another approach using Counter
        sDict= Counter(s)
        for i in t:
            if i not in sDict:
                return False
            sDict[i]-=1
            if sDict[i]==0:
                sDict.pop(i)
        return not sDict
