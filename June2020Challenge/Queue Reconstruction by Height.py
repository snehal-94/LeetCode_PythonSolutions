Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Solution___________________________________________________________________

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #sorting the list in decreasing order of height and increasing order of k
        people=sorted(people,key=lambda i:(-i[0],i[1]))
        res=[]
        #After sorting, inserting all the heights at the respective k indices. It's because if a smaller height 
        #gets in between 2 bigger heights, it doesn't matter to the bigger height
        #but matters to smaller height
        for i,j in people:
            res.insert(j,[i,j])
        return res
