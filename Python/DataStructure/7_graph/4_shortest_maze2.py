'''
到达二维矩阵的洞的最短路径
'''

import heapq

dic = {'r': [0, 1], 'l': [0, -1], 'u': [-1, 0], 'd': [1, 0]}

def is_valid(x, y, matrix):
    m = len(matrix)
    n = len(matrix[0])
    return x >= 0 and y >= 0 and x < m and y < n and not matrix[x][y]

def get_neighbors(matrix, node, end):
    new_x = node[0]
    new_y = node[1]
    for key in dic:
        dis = 0
        flag = None
        while is_valid(new_x, new_y, matrix):
            if (new_x, new_y) == end:
                flag = True
                break
            new_x += dic[key][0]
            new_y += dic[key][1]
            dis += 1
        
        if flag or [new_x, new_y] != node:
            yield dis, (new_x, new_y), key


# 贪心算法
def maze_sol(matrix, start, end):
    pq = [(0, start, '')]
    visited = set()

    while pq:
        dis, node, direct = heapq.heappop(pq)
        visited.add((node[0], node[1]))

        if node == end:
            return direct

        for dis, nbr, dir in get_neighbors(matrix, node, end):
            if (nbr[0], nbr[1]) not in visited:
                heapq.heappush(pq, (dis, nbr, direct+dir))
    
    return False


'''
另一种解法
'''

import heapq

def findShortestWay(maze, ball, hole):
    dirs = {'u' : (-1, 0), 'r' : (0, 1), 'l' : (0, -1), 'd': (1, 0)}

    def neighbors(maze, node):
        for dir, vec in dirs.items():
            cur_node, dist = list(node), 0
            while 0 <= cur_node[0]+vec[0] < len(maze) and \
                  0 <= cur_node[1]+vec[1] < len(maze[0]) and \
                  not maze[cur_node[0]+vec[0]][cur_node[1]+vec[1]]:
                cur_node[0] += vec[0]
                cur_node[1] += vec[1]
                dist += 1
                if tuple(cur_node) == hole:
                    break
            yield tuple(cur_node), dir, dist

    heap = [(0, '', ball)]
    visited = set()
    while heap:
        dist, path, node = heapq.heappop(heap)
        if node in visited: continue
        if node == hole: return path
        visited.add(node)
        for neighbor, dir, neighbor_dist in neighbors(maze, node):
            heapq.heappush(heap, (dist+neighbor_dist, path+dir, neighbor))

    return "impossible"

if __name__=="__main__":
    matrix = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    dest  = (1, 4)
    findShortestWay(matrix, start, dest)