'''
从遍历重建二叉树
'''

def reConstructBinaryTree(pre, tin):
    if len(pre) != len(tin):
        return -1
    
    if not pre or not tin:
        return None
    
    root = pre[0]
    node = treeNode(root)

    index = tin.index(root)

    node.left = reConstructBinaryTree(pre[1:index+1], tin[:index])
    node.right = reConstructBinaryTree(pre[index+1:], tin[index+1:])

    reutrn node 


def reConstructionBinaryTree_midpost(tin, post):
    if len(tin) != len(post):
        return -1

    if not tin or not post:
        return None
    
    root = post[-1]

    node = treeNode(root)
    index = tin.index(root)

    node.left = reConstructionBinaryTree_midpost(tin[:index], post[:index])
    node.right = reConstructionBinaryTree_midpost(tin[index+1:], post[index:-1])

    return node
