class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:

    def __init__(self):
        self.root = TrieNode()

    def longestCommonPrefix(self, strs: list[str]) -> str:

        # Insert all words into Trie
        def insert(word):
            node = self.root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            # This word ends here
            node.is_end = True


        # Build the Trie
        for word in strs:
            insert(word)


        # Find the common prefix
        def ans():
            result = ""
            node = self.root

            while True:

                # If this node is the end of a word,
                # we cannot go further.
                if node.is_end:
                    break

                # If there isn't exactly ONE child,
                # the common prefix stops.
                if len(node.children) != 1:
                    break

                # Get the only child
                key = next(iter(node.children))

                # Add that character to our answer
                result += key

                # Move one step ahead in the Trie
                node = node.children[key]

            return result


        return ans()