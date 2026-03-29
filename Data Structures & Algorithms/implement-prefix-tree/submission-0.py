class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for i in word:
            index = ord('a') - ord(i)
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEnd = True


    def search(self, word: str) -> bool:
        curr = self.head
        for i in word:
            index = ord('a') - ord(i)
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for i in prefix:
            index = ord('a') - ord(i)
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True
        