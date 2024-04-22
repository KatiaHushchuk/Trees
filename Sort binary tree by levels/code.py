def tree_by_levels(node):
    if not node:
        return []
    res = []
    level = [node]
    while level:
        next_level = []
        for current in level:
            res.append(current.value)
            if current.left:
                next_level.append(current.left)
            if current.right:
                next_level.append(current.right)
        level = next_level
    return res
  
