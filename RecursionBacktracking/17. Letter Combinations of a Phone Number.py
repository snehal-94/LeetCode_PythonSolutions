Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.


Solution
________________________________________________

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dict={
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        stack=[]
        dig=[dict[int(i)] for i in digits]
        
        def rec(curr,dig):
            if not dig:
                stack.append(curr)
                return
            else:
                for letter in dig[0]:
                    rec(curr+letter,dig[1:])
        rec("",dig)
        return stack     
                    
                        
        
