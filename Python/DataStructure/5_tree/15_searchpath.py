'''
路径搜索
'''


''''
给定一棵二叉树和一个和，确定树是否有根到叶的路径，
这样沿路径加起来的所有值等于给定的总和.
'''
def hasPathSumHelper(node, target):
    if node is None:
        return False

    if node.left is None and node.right is None and node.value == target:
        return True

    return hasPathSumHelper(node.left, target-node.value) or \
        hasPathSumHelper(node.right, target-node.value)


def hasPathSum(target):
    return hasPathSumHelper(proot, target)


'''
给定一棵二叉树和一个和，确定树是否有根到叶的路径，
这样沿路径加起来的所有值等于给定的总和.并打印路径
'''
def hasPathSum2Helper(proot, target):
    if proot is None:
        return -1

    tmp_res = res = []

    flag = dfs(proot, target, tmp_res, res)
    return res

def dfs(node, target, tmp_res, res):
    if node is None:
        return False
    
    if node.left is None and node.right is None and node.value == target:
        tmp_res.append(node)
        res.append(tmp_res)
        return True

    if node.left:
        return dfs(node.left, tmp_res + [node.value], res, target - node.value)
    if node.right:
        return dfs(node.right, tmp_res + [node.value], res, target - node.value)

    
        
