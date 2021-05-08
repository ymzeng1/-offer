# 双指针
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        res = pre = head
        cur = head.next
        while cur.val != val and cur:
            pre.next = cur
            pre = cur
            cur = cur.next
        pre.next = cur.next
        return res
