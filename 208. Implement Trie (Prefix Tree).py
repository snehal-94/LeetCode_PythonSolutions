Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

Solution
_________________________________________________

        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord=False
        self.children={}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr=self
        for w in word:
            if w not in curr.children:
                curr.children[w]=Trie()
            curr=curr.children[w]
        curr.isWord=True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr=self
        for w in word:
            if w not in curr.children:
                return False
            curr=curr.children[w]
        if curr.isWord==True:
            return True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr=self
        for w in prefix:
            if w not in curr.children:
                return False
            curr=curr.children[w]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
