class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return None
        if root == p or root == q: return root                         #若根节点为空、根节点为两个节点之一
        left = self.lowestCommonAncestor(root.left, p, q)              #遍历左子树，返回先找到的p、q之一
        right = self.lowestCommonAncestor(root.right, p, q)            #遍历右子树，返回先找到的p、q之一
        if not left: return right     #左子树无p、q时，遍历说明p、q全在右边
        if not right: return left     #右子树无p、q时，遍历说明p、q全在左边
        return root                   #两边都不为空，说明根节点，为最近公共节点
