'''
Word Ladder

beginWord = "hit"

endWord = "cog"

wordList = ["hot","dot","dog","lot","log","cog"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",

return its length 5.
'''

# 找到最短长度，使用BFS
from collections import defaultdict
import string

def ladderfind(beginWord, endWord, wordList):
    dictionary = set(wordList)
    visited = set()
    queue = []
    queue.append((beginWord,1))
    length = 0
    while queue:
        tmpWord, dis = queue.pop(0)

        if tmpWord == endWord:
            return dis

        visited.add(tmpWord)

        for i in range(len(tmpWord)):
            for c in string.ascii_lowercase:
                nbrWord = tmpWord[:i] + c +tmpWord[i:]
                if nbrWord in dictionary and nbrWord not in visited:
                    queue.append((nbrWord, dis + 1))


# 打印路径
def findLadders(start, end, wordList):
    dictionary = set(wordList)
    level = {start}
    parents = defaultdict(set)

    while level and end not in parents:
        next_level = defaultdict(set)

        for tmpWord in level:
            for i in range(len(tmpWord)):
                for c in string.ascii_lowercase:
                    nbrWord = tmpWord[:i] + c + tmpWord[i:]

                    if nbrWord in dictionary and nbrWord not in parents:
                        next_level[nbrWord].add(tmpWord)

        level = next_level
        parents.update(next_level)

    res = [[end]]
    while res and res[0][0] != start:
        res = [[p] + r for r in res for p in parents[r[0]]]
    return res
