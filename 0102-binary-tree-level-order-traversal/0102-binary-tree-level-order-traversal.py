# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:    
        if root is None:
            return []
        queue = [(root, 1)]
        values = []
        while len(queue):
            v, level = queue.pop(0)
            if v.left:
                queue.append((v.left, level+1))
            if v.right:
                queue.append((v.right, level+1))
            if len(values) < level:
                values.append([v.val])
            else:
                values[level-1].append(v.val)
        return values