Given an array w of positive integers, where w[i] describes the weight of index i, 
write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. 
Solution's constructor has one argument, the array w. pickIndex has no arguments.
Arguments are always wrapped with a list, even if there aren't any.

Solution_______________________________________________________________

class Solution:  
    def __init__(self, w: List[int]):  
        self.s=[]
        cumSum=0
        for i in w:
            cumSum+=i
            #creating the list using cumulative sum.
            self.s.append(cumSum)
        self.total=cumSum

    def pickIndex(self) -> int:
        #a random float no. between 1 and 0 is generated.
        #Multiply it with the max sum to get the final random num
        
        randNum=self.total*random.random()
        l,h=0,len(self.s)
        while l<h:
            m=l+(h-l)//2
            if randNum>self.s[m]: l=m+1
            else: h=m
        return l



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
