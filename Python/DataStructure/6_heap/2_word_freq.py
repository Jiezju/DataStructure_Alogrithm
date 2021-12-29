'''
最大词频统计
'''
import heapq


class Element:
    def __init__(self, word, count):
        self._count = count
        self._word = word

    def __lt__(self, other):
        if self._count == other._count:
            return self._word < other._word
        return self._count < other._count

    def __eq__(self, other):
        return self._count == other._count and self._word == other._word


def topKFrequent(words, k):
    dic = {}
    for word in words:
        dic[word] = dic.setdefault(word, 0) + 1

    heap = []
    res = []
    for word, count in dic.items():
        heapq.heappush(heap, Element(word, -count))

        if len(heap) > (len(dic) - k):
            res.append(heapq.heappop(heap)._word)

    return res


if __name__ == '__main__':
    words = ["i", "love", "you", "i", "love", "coding", "i", "like", "sports"]
    k = 2
    print(topKFrequent(words, k))
