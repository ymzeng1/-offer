class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.res = []
        def recur(cur):
            if not cur: return 
            recur(cur.right)
            self.res.append(cur.val)
            recur(cur.left)
        recur(root)
        return self.res[k-1]
      
# 自己写出来的！
