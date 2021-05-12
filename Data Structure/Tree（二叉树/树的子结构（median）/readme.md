recur(A, B) 函数：

终止条件：
当节点 BB 为空：说明树 BB 已匹配完成（越过叶子节点），因此返回 truetrue ；
当节点 AA 为空：说明已经越过树 AA 叶子节点，即匹配失败，返回 falsefalse ；
当节点 AA 和 BB 的值不同：说明匹配失败，返回 falsefalse ；
返回值：
判断 AA 和 BB 的左子节点是否相等，即 recur(A.left, B.left) ；
判断 AA 和 BB 的右子节点是否相等，即 recur(A.right, B.right) ；


isSubStructure(A, B) 函数：

特例处理： 当 树 AA 为空 或 树 BB 为空 时，直接返回 falsefalse ；
返回值： 若树 BB 是树 AA 的子结构，则必满足以下三种情况之一，因此用或 || 连接；
以 节点 AA 为根节点的子树 包含树 BB ，对应 recur(A, B)；
树 BB 是 树 AA 左子树 的子结构，对应 isSubStructure(A.left, B)；
树 BB 是 树 AA 右子树 的子结构，对应 isSubStructure(A.right, B)；
