Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
Solution__________________________________________
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s==" " or len(s)==1:return 1
        stack,m=[],0
        for i in s:
            if i in stack:
                stack=stack[stack.index(i)+1:]
            stack.append(i)
            m=max(m,len(stack))
        return m
