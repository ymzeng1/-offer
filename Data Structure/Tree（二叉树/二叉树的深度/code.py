# BFS 层序遍历
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [root]
        res = 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1
        return res
      

# DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
