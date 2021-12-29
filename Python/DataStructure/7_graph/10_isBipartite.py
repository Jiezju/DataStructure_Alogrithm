'''
着色法判断二分图
'''

def isBipartite(graph):
    color = {}

    def dfs(i):
        for nbr in graph[i]:
            if nbr not in color:
                color[nbr] = -color[i]
            
            if color[nbr] == color[i]:
                return False
            
            if not dfs(nbr):
                return False
        return True

    for i in range(len(graph)):
        # 没有着色，进行着色
        if i not in color:
            color[i] = 1
        
        # dfs 对相邻的着另一种颜色，并递归下去
        if not dfs(i):
            return False

    return True
