# 最优解法
# 设置两个指针，cur 指向链表头节点，pre 指向空
# 暂存 cur 的后继节点，tmp = cur.next
# 将 cur.next 反指向pre
# 将 pre 指向 cur，即 pre 指针后移
# 将 cur 指向 2 中暂存的 tmp 节点，即 cur 指针后移 循环 第2 到 5 步，直到 cur 遍历完整个链表
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        return pre
