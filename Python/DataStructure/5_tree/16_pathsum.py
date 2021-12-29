'''
给你一个二叉树，其中每个节点都包含一个整数值.
查找总和给定值的路径数量.
路径不需要在根或叶上开始或结束，但必须向下（仅从父节点到子节点）.
'''


def findPath(node, target):
    if node == NULL:
        return 0
    
    res = 0
    if node.val == target:
        res += 1
    
    res += findPath(node.left, target-node.val)
    res += findPath(node.right, target-node.val)
    
    return res
    	
def pathSum(node, target):
    if node == None:
        return 0
    
    res = findPath(node, target)
    res += pathSum(node.left, target)
    res += pathSum(node.right, target)
    
    return res
