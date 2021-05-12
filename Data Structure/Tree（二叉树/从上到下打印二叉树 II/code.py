class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = collections.deque([root])
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
      
      ##第一次靠自己写出完美答案！！！
