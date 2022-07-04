Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

_____________________________________________________________________________________

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
#         Time Complexity: O(N). We process each character in both the strings exactly once to determine if the strings are isomorphic.
# Space Complexity: O(1) since the size of the ASCII character set is fixed and the keys in our dictionary are all valid ASCII characters according to the problem statement.

#         mapS_t={}
#         mapT_s={}
# #       Use zip to create tuples from 2 iterators
#         for i,j in zip(s,t):
# #         If no mapping exists in either of dictionaries
#             if (i not in mapS_t) and (j not in mapT_s):
#                 mapS_t[i]=j
#                 mapT_s[j]=i
            
# #             If mapping doesn't exist in the dictionaries/ mapping exists but doesn't match
# #               in either dictionaries or both
#             elif mapS_t.get(i) != j or mapT_s.get(j) != i:
#                 return False
#         return True

#     One Liner
        # return len(set(s))==len(set(t))==len(set(zip(s,t)))
        
#        We use a method called first occurence transformation. i.e we replace characters in a string with the index of it's first occurence. Like PAPER becomes 01034 and title becomes 01034.Hence, both are isomorphic. Instead of putting values in string we will use a list because in longer strings there could be issue with indexes that are>9 i.e 10, 11, etc
#         Complexity O(N)
        dict_s={}
        dict_t={}
        list_s=[]
        list_t=[]
        for i,letter in enumerate(s):
            if letter not in dict_s:
                dict_s[letter]=i
            list_s.append(dict_s[letter])
        for i,letter in enumerate(t):
            if letter not in dict_t:
                dict_t[letter]=i
            list_t.append(dict_t[letter])
        return list_t==list_s


