class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        res = []

        m = len(board)
        n = len(board[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        # ---------------- BUILD TRIE ----------------

        root = TrieNode()

        for word in words:

            node = root

            for char in word:

                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            # Instead of only is_end = True,
            # store the complete word here.
            node.word = word


        # ---------------- DFS ----------------

        def dfs(i, j, node):

            # Current board character
            char = board[i][j]

            # If this character doesn't exist in Trie,
            # this path cannot form any word.
            if char not in node.children:
                return

            # Move to the Trie node corresponding
            # to the current character.
            node = node.children[char]


            # If a complete word ends here,
            # we found a word.
            if node.word:
                res.append(node.word)

                # Prevent adding the same word again.
                node.word = None


            # Mark current board cell as visited
            board[i][j] = '#'


            # Explore all 4 directions
            for di, dj in directions:

                ni = i + di
                nj = j + dj

                if 0 <= ni < m and 0 <= nj < n:

                    if board[ni][nj] != '#':
                        dfs(ni, nj, node)


            # BACKTRACK
            # Restore the original character
            board[i][j] = char


        # Start DFS from every cell
        for i in range(m):
            for j in range(n):

                dfs(i, j, root)


        return res