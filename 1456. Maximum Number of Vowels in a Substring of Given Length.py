Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
Example 4:

Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.
Example 5:

Input: s = "tryhard", k = 4
Output: 1
 

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length

Solution________________________________________

from collections import Counter
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow=['a','e','i','o','u']
        count=Counter(s[:k])
        j=k
        m,tot=0,0
        for i in count:
            if i in vow:
                tot+=count[i]  
        m,tot=tot,0
        x=0
        while j<=len(s):
            if j==len(s):
                break
            count[s[x]]-=1
            if(count[s[x]]<=0):
                count.pop(s[x])
            if s[j] in count:
                count[s[j]]+=1
            else:
                count[s[j]]=1
            if j<len(s):
                for i in count:
                    if i in vow:
                        tot+=count[i]
                if tot>m:
                    m=tot
            j+=1
            x+=1
            tot=0
        return m
