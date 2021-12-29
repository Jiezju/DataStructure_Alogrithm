'''
python 堆
'''

# 使用heappush创建堆
import heapq
from heapq import heappush, heappop

heap = []
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for item in data:
    heappush(heap, item)

print(heap)

data = [1, 5, 3, 2, 8, 5]
heapq.heapify(data)  # 默认最小堆
print(data)

# K大（小）
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
heapq.heapify(li1)
print(heapq.nlargest(3, li1))
print(heapq.nsmallest(3, li1))

heap = []
data = [(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')]
for item in data:
    heappush(heap, item)

while heap:
    item = heappop(heap)
    print(item[0], ": ", item[1])
