class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_empty = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char] 
        node.is_empty = True       

    def search(self, word: str) -> bool:
        
        def dfs(node, idx):
            if idx == len(word):
                return node.is_empty

            char = word[idx]    
            
            if char != '.':
                if char not in node.children:
                    return False

                return dfs(node.children[char], idx+1)

            else:
                for child in node.children.values():
                    if dfs(child, idx+1):
                        return True

            return False

        return dfs(self.root, 0)                        

