'''
其他数据结构转二叉树
'''

def sortedArrayToBST(num):
    if not num:
        return None

    mid = len(num) // 2

    node = TreeNode(num[mid])

    node.left = sortedArrayToBST(num[:mid])
    node.right = sortedArrayToBST(num[mid+1:])

    reutrn node


def sortedListToBST(head):
    if head is None:
        return None

    slowpt = fastpt = head

    while slowpt and fastpt.next:
        midnode = slowpt
        slowpt = slowpt.next
        fastpt = fastpt.next.next

    node = TreeNode(midnode.value)

    node.left = sortedListToBST(head)
    node.right = sortedListToBST(slowpt.next)

    return node

