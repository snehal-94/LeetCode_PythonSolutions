Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
Solution
_______________________________________________

class Solution:
    def frequencySort(self, s: str) -> str:
        count={}
        for i in s:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        revSort=sorted(count.items(),key=lambda x:x[1],reverse=True)
        res=''
        for i in revSort:
            res+=i[0]*i[1]
        return res
