class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        for ch in word:
            index = ord(ch) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.isEnd

            ch = word[i]
            if ch == '.':
                # Try all possible children
                for child in node.children:
                    if child and dfs(child, i + 1):
                        return True
                return False
            else:
                index = ord(ch) - ord('a')
                child = node.children[index]
                if not child:
                    return False
                return dfs(child, i + 1)

        return dfs(self.head, 0)
