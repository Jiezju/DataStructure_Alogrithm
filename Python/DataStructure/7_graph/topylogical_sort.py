'''
拓扑排序
'''

def TopologicalSort(G):
    # init
    in_degree = dict((u,0) for u in G)

    for u in G:
        # G[u] 存储了 u 的出度节点 v 是 u 的出度（u是v的入度）
        for v in G[u]:
            in_degree[v] += 1

    queue = []

    for u in G:
        if in_degree[u] == 0:
            queue.append(u)
    
    res = []

    while queue:
        node = queue.pop(0)
        res.append(node)

        for v in G[node]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    return res

if __name__=="__main__":
    # 定义图结构
    graph = {
        "A": ["B","C"], # A的指向的元素为B、C
        "B": ["D","E"], # B的指向的元素为D、E
        "C": ["D","E"], # D的指向的元素为F
        "D": ["F"],     # E的指向的元素为F
        "E": ["F"],     # F的指向的元素为空
        "F": [],
    }

    TopologicalSort(graph)

