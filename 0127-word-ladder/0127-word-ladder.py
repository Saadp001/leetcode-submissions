from collections import deque
from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        lvl = 1
        q = deque([beginWord])
        visited = {beginWord}

        while q:
            len_q = len(q)

            for _ in range(len_q):
                curr = q.popleft()

                if curr == endWord:
                    return lvl

                for i in range(len(curr)):
                    for new in ascii_lowercase:
                        new_word = curr[:i] + new + curr[i+1:]

                        if new_word in words and new_word not in visited:
                            visited.add(new_word)
                            q.append(new_word)

            lvl += 1

        return 0