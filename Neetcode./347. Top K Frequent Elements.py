Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
  _________________________________________________________________________________________________________
  
  
  class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#       Complexity  O(N) Brute force
        result={}
        res=[]
        for num in nums:
            if num not in result:
                result[num]=1
            else:
                result[num]+=1
        for a,b in sorted(result.items(), key=lambda x: x[1], reverse= True):
            if k>0:
                res.append(a)
                k-=1
        return res
       
    _________________________________________________________________________________________________________
    
    #         Using most_common() function 
        count=Counter(nums).most_common()
        return [count[i][0] for i in range(k)]
