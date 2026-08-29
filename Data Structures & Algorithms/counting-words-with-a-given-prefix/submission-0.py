class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, length):
        current = self.root
        for i in range(length):
            if word[i] not in current.children:
                current.children[word[i]] = TrieNode()
            current = current.children[word[i]]
            current.count += 1
    
    def count(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]

        return current.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()

        for word in words:
            if len(word) >= len(pref):
                trie.add(word, len(pref))
        return trie.count(pref)