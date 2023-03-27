# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val == q.val:
            return root
        path1 = self.path(root, p)
        path2 = self.path(root, q)
        
        i, j = len(path1)-1, len(path2)-1
        while i>=0 and j>=0:
            if path1[i].val == path2[j].val:
                return path1[i]
            elif i > j:
                i -= 1
            else:
                j -= 1       

    def path(self, root, target):
        path = []
        while root.val != target.val:
            path.append(root)
            if target.val > root.val:
                root = root.right
            else:
                root = root.left
        path.append(root)
        return path