'''
 A*算法 (默认网格搜索问题)
'''

import heapq
import math

def init_distance(G, start):
    distance = {start: 0}
    for node in G:
        if node is not start:
            distance[node] = math.inf

    return distance

def get_neibours(graph, current_node):
    m = len(graph)
    n = len(graph[0])
    x = current_node.x
    y = current_node.y
    result = []

    for i, j in [[x - 1, y], [x + 1, j], [x, y - 1], [x, y + 1]]:
        if i < m and j < n and graph[i][j] != '#':  # 表示非路障
            result.append([i, j])

    return result

def heuristic(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)


def A_star(graph, start, goal):
    # 记录from节点
    come_from = {}
    come_from[start] = None

    # 初始化每个node到start的距离
    init_distance(graph, start)

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    visited = set()

    while priority_queue:
        dis, cur_node = heapq.heappop(priority_queue)
        visited.add(node)

        if cur_node == goal:
            break

        for node in get_neibours(graph, cur_node):
            if node not in visited:
                if distance[cur_node] + get_weight(cur_node, node) < distance[node]:
                    distance[node] =  distance[cur_node] + get_weight(cur_node, node)
                    F_cost = distance[node] + heuristic(node, goal)  # 启发式获取当前点到终点的距离
                    heapq.heappush((node, F_cost))
                    come_from[node] = cur_node

    return come_from, distance
