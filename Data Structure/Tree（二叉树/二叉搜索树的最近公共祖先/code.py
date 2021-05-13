class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return 
        if (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        if (q.val < root.val and p.val < root.val): 
            return self.lowestCommonAncestor(root.left, p, q)
        else: 
            return root
          
      
