class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        start = head
        res = []
        while start:
            res.append(start.val)
            start = start.next
        return res[::-1]
