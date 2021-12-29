'''
从数据流中找到中位数
'''
import heapq


class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, item):
        large, small = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, -item))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))

    def getMedian(self):
        large, small = self.heaps
        if len(large) > len(small):
            return -large[0]

        return (small[0] - large[0]) / 2.0

if __name__ == '__main__':
    finder = MedianFinder()
    finder.addNum(2)
    finder.addNum(3)
    finder.addNum(4)
    finder.addNum(5)
    print(finder.getMedian())
