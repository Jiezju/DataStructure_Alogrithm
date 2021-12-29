'''
搜索模板
'''

# recursion
def dfs(root):
    result = []
    visited = set()
    dfs_helper(root, result, visited)
    return result

def dfs_helper(node, result, visited):
    visited.add(node)
    result.append(node)

    for nod in node.getConnections():
        if nod not in visited:
            dfs_helper(nod, result, visited)


def dfs_(root):
    stack = [root]
    visited = set()
    visited.add(root)

    while stack:
        node = stack.pop()
        print(node)

        for nod in node.getConnections():
            if nod not in visited:
                stack.append(nod) 
                visited.add(nod)      

def bfs(root):
    queue = [root]
    visited = set()
    visited.add(root)

    while queue:
        node = queue.pop(0)
        print(node)

        for nod in node.getConnections():
            if nod not in visited:
                queue.append(nod)
                visited.add(nod)
        
