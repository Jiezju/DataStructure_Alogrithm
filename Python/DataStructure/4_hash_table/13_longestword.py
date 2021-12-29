'''
words = ["w","wo","wor","worl", "world"]

Output: "world"
'''


def longestWord(words):
    words = sorted(words)

    visited = set()
    res = ''

    for word in words:
        if len(word) == 1 or word[:-1] in visited:
            visited.add(word)
            if len(word) > len(res):
                res = word

    return res


if __name__ == '__main__':
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(longestWord(words))
