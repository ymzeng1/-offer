class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = collections.deque([root])
        i = 0
        while queue:
            tmp = []
            i += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if i%2 == 0: tmp = tmp[::-1]
            res.append(tmp)
        return res
