# 伪头节点法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dum = ListNode(0) ##重点理解
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next
      
     
#递归法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        pre = None
        if l1.val < l2.val:
            pre = l1
            pre.next = self.mergeTwoLists(l1.next, l2)
        else:
            pre = l2
            pre.next = self.mergeTwoLists(l1, l2.next)
        return pre
