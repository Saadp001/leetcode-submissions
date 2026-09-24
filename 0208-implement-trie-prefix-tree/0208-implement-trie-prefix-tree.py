class TrieNode:
    def __init__(self):
        # Stores the next characters.
        # Example:
        # "apple" -> a -> p -> p -> l -> e
        self.children = {}

        # True only when a complete word ends at this node.
        self.is_end = False


class Trie:

    def __init__(self):
        # Empty starting node.
        # It doesn't represent any character.
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        # Start from the root.
        node = self.root

        # Go through every character of the word.
        for char in word:

            # If this character doesn't exist,
            # create a new TrieNode for it.
            if char not in node.children:
                node.children[char] = TrieNode()

            # Move to the node representing this character.
            node = node.children[char]

        # We have reached the end of the word.
        # Mark this node as the end of a complete word.
        node.is_end = True


    def search(self, word: str) -> bool:
        # Start from root.
        node = self.root

        # Follow the path of the word.
        for char in word:

            # If the character doesn't exist,
            # the word was never inserted.
            if char not in node.children:
                return False

            # Move to the next character's node.
            node = node.children[char]

        # Reaching the node isn't enough.
        # We also need to know whether a complete word
        # actually ends here.
        return node.is_end


    def startsWith(self, prefix: str) -> bool:
        # Start from root.
        node = self.root

        # Follow the characters of the prefix.
        for char in prefix:

            # If any character is missing,
            # no word starts with this prefix.
            if char not in node.children:
                return False

            # Move to the next node.
            node = node.children[char]

        # We successfully followed the entire prefix.
        # Therefore, some inserted word has this prefix.
        return True