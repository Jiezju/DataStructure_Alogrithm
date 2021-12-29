'''
Dijstra
'''

import heapq
import math

def init_distance(G, start):
    distance = {start:0}

    for node in G:
        if node is not start:
            distance[node] = math.inf

def Dijstra(G, start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    visited = set()

    distance = init_distance(G, start)
    parent = {start:start}

    while priority_queue:
        dis, node = heapq.heappop(priority_queue)
        visited.add(node)

        for nbr in node.neighbors():
            if nbr not in visited:
                if dis + G.getdis(node, nbr) < distance[nbr]:
                    distances[nbr] = dis + G.getdis(node, nbr)
                    parent[nbr] = node
                    heapq.heappush(priority_queue, (distances[nbr], nbr))

