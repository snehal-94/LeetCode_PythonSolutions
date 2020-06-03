Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Solution
________________________________________________

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0: return ['']
        result = ['()']
        for pair in range(1,n):
            temp = []
            for x in result:
                for i in range(len(x)):
                    temp.append(x[:i] + '()' + x[i:])
            result = list(set(temp))
        return result
                    
