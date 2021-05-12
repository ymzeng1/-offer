#递归
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

#Python 利用平行赋值的写法（即 a, b = b, aa,b=b,a ），可省略暂存操作。其原理是先将等号右侧打包成元组 (b,a)(b,a), 再序列地分给等号左侧的 a,b 序列。


#辅助栈（队列）
