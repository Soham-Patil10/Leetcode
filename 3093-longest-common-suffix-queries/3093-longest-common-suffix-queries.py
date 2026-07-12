class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = 0
        self.best_len = float('inf')

def insert(root, word, idx):
    node = root
    if len(word) < node.best_len:
        node.best_len = len(word)
        node.best_idx = idx
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        if len(word) < node.best_len:
            node.best_len = len(word)
            node.best_idx = idx

def query(root, word):
    node = root
    for char in word:
        if char not in node.children:
            return node.best_idx
        node = node.children[char]
    return node.best_idx

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()
        
        for i, word in enumerate(wordsContainer):
            insert(root, word[::-1], i)
        
        ans = []
        for word in wordsQuery:
            ans.append(query(root, word[::-1]))
        return ans