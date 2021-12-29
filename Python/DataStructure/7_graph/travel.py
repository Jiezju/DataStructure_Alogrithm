# 深度优先遍历 递归
def dfs(G, node, visited):
    visited.add(node)
    
    for nbr in G.get_ngbs(node):
        if nbr in visited:
            continue
        dfs(G, nbr, visited)

def DFSTraversal(G):
    visited = set()
    for node in G.get_vertex:
        if node not in visited:
            dfs(G, node, visited)

# 深度优先遍历 迭代
def dfsIterative(G, start, dest):
    stack = []
    visited = set()
    parent = {}
    stack.append(start)
    visited.add(start)
    
    while stack:
        cur = stack.pop()
        
        if cur == dest:
            return parent
        
        for nbr in G.get_ngbs(cur):
            if nbr not in visited:
                stack.append(nbr)
                visited.add(nbr)
                parent[nbr] = cur

# 广度优先遍历
from collections import deque

def bfs(G, start, dest):
    queue = deque()
    visited = set()
    parent = {}
    queue.append(start)
    
    while queue:
        cur = queue.popleft()
        
        if cur == dest:
            return parent
        
        for nbr in G.get_ngbs(cur):
            if nbr not in visited:
                queue.append(nbr)
                visited.add(nbr)
                parent[nbr] = cur   

# Dijstra 算法
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
        dis, cur  = heapq.heappop(priority_queue)
        visited.add(cur)
        
        for nbr in cur.neibours():
            if nbr not in visited:
                if dis + getdis(cur, nbr) < distance[nbr]:
                    distance[nbr] = dis + getdis(cur, nbr)
                    parent[nbr] = cur 	
                    heapq.heappush(priority_queue, (distance[nbr], nbr))

