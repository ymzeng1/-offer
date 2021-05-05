# 快慢指针
# 先让快指针走k步，然后让快慢指针一起走，直到快指针到尽头
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        front = head
        behind = head
        while k > 0:
            front = front.next
            k-=1

        while front:
            front = front.next
            behind = behind.next

        return behind
