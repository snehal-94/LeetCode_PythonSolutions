// A pangram is a sentence where every letter of the English alphabet appears at least once.

// Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

// Example 1:

// Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
// Output: true
// Explanation: sentence contains at least one of every letter of the English alphabet.
// Example 2:

// Input: sentence = "leetcode"
// Output: false
 

// Constraints:

// 1 <= sentence.length <= 1000
// sentence consists of lowercase English letters.

_____________________________________________________________________

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
#         Brute force One liner
          return len(set(sentence))==26

#     Optimised with list O(n)
        res=[]
        for letter in  sentence:
            if letter not in res:
                res.append(letter)
        return len(res)==26
