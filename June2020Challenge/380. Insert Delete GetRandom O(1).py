Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

Solution_________________________________________________________________

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.stack=set()
        
        #Using stack and dict
        self.stack=[]
        self.dict={}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        #USING SET
        # if val not in self.stack:
        #     self.stack.add(val)
        #     return True
        
        #Using dict and stack
        # Retrieving from dictionaries is faster than from stack
        if val not in self.dict:
            self.dict[val]=len(self.stack)
            self.stack.append(val)
            
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        #USING SET
        # if val in self.stack:
        #     self.stack.remove(val)
        #     return True
        
        #Using stack and dict
        if val in self.dict:
            #placing the last element of stack in the val's place
            #and delete the last element
            self.dict[self.stack[-1]]=self.dict[val]
            self.stack[self.dict[val]]=self.stack[-1]
            self.stack.pop()
            self.dict.pop(val)
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        #Using set is slow for random selection 
        #since it needs to be converted to list
        # return random.choice(list(self.stack))
        
        #Using stack and dict
        return random.choice(self.stack)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
