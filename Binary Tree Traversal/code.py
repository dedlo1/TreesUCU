class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Pre-order traversal
def pre_order(node):
    if not node:
        return []
    root = node.data
    left = pre_order(node.left) if node.left else []
    right = pre_order(node.right) if node.right else []
    return [root] + left + right

# In-order traversal
def in_order(node):
    if not node:
        return []
    root = node.data
    left = in_order(node.left) if node.left else []
    right = in_order(node.right) if node.right else []
    return left + [root] + right

# Post-order traversal
def post_order(node):
    if not node:
        return []
    root = node.data
    left = post_order(node.left) if node.left else []
    right = post_order(node.right) if node.right else []
    return left + right + [root]
