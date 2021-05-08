# 浪漫相遇法
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1 = headA
        node2 = headB
        while node1 != node2:
            node1 = node1.next if node1.next != None else headB
            node2 = node2.next if node2.next != None else headA
        return node1
