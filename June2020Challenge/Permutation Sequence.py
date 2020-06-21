The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

Solution_________________________________________________________________

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
My solution is basically the same with the many others but here is another explanation:

Let's go over an example:

n=4  k=9
1234 ------ start here
1243 ------ third digit changes here 
1324 ------ second digit changes here 
1342
1423
1432 
2134 ------ first digit changes here 
2143
2314 -> k=9
2341
2413
2431
3124 ------ first digit changes here 
.
.
.
As you can see first digit changes after 6 occurances which is (n-1)! and the second digit changes after 2 occurances which is (n-2)!. 
Similarly third digit changes after 1 occurances which is (n-3)!. 
Is this a coincidance? Of course not. Since it is a permutation we compute it like this:
(n)(n-1)(n-2)...(1) each paranthesis represents a digit. for the first place, we have n options. 
After using one of the numbers, we cannot use it again. So we have n-1 number options for the second place. 
In the end we multiply them to get the total number of permutations. Let's say we picked '1' for the first place. 
now we have (n-1)! options for the rest of the number. This is why at each step a number is repeated that many time.

Let's go back to our example:

Since the first digit is repeated (n-1)! times, by dividing the k by n we can find our first digit. 
Division must be integer division because we are only interested in the integer part.

k=9, n=4
(n-1)! = 6
k /(n-1)!  = 1
remainder = 3
Numbers that we can use as digits are = [1,2,...,n]

So, our first digit is the digit at index 1 which is 2. 
We take the digit at 1 because our list is sorted so we are sure that the second smallest digit is at index 1.

Since we used 2, we need to remove it from our list and k takes the value of the remainder. 
You can think of lit ike this: we decided on our first digit so we can discard that part and deal with the rest of the number. 
As you can see the problem is the same! but this time we have (n-2)! instead of (n-1)!,
k=remainder and we have one less number in our list.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factor = factorial(n-1)
        k -= 1 # index starts from 1 in the question but our list indexs starts from 0
        ans = []
        numbers_left = list(range(1,n+1))
        
        for m in range(n-1,0,-1):
            index = int(k // factor)
            ans += str(numbers_left[index])
            numbers_left.pop(index)
            k %= factor
            factor /= m
            
        ans += str(numbers_left[0])
        return ''.join(ans)
        
