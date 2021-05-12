class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res

      
#自己的错误写法
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        queue = [root] ###应该用 collections.deque([root])
        while queue:
            node = queue.pop() ###应该用 popleft()
            res.append(node.val)
            if node.right: queue.append(node.right) 
            if node.left: queue.append(node.left) 
        return res
