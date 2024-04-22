class Node:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

def pre_order(node):
    if not node:
        return []
    res = []
    res.append(node.data)
    res.extend(pre_order(node.left))
    res.extend(pre_order(node.right))
    return res

def in_order(node):
    if not node:
        return []
    res = []
    res.extend(in_order(node.left))
    res.append(node.data)
    res.extend(in_order(node.right))
    return res

def post_order(node):
    if not node:
        return []
    res = []
    res.extend(post_order(node.left))
    res.extend(post_order(node.right))
    res.append(node.data)
    return res
