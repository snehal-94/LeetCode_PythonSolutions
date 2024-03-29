Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

________________________________________________________________

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         Brute force optimal O(N)
        result={}
        for word in strs:
            sortedWord=str(sorted(word))
            if sortedWord not in result:
                result[sortedWord]=[word]
            else:
                result[sortedWord].append(word)
        return list(result.values())
       
      
#     Without using sorted Time: O(mn) and Space: O(n)
        result= defaultdict(list)
        
        for word in strs:
            asciiArray=[0] * 26
            for ch in word:
                asciiArray[ord(ch) - ord("a")]+=1
            result[tuple(asciiArray)].append(word)
        return list(result.values())
