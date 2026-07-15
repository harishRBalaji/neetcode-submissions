class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            index = ord(char) - ord('a')
            if current.children[index] is None:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            index = ord(char) - ord('a')
            if current.children[index] is None:
                return False
            current = current.children[index]
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if current.children[index] is None:
                return False
            current = current.children[index]
        return True
        