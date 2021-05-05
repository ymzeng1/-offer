# solution 1
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        start = head
        res = []
        while start:
            res.append(start.val)
            start = start.next
        return res[::-1]

    
# solution 2
class Solution:
def reversePrint(self, head: ListNode) -> List[int]:
    stack = []
    while head:
        stack.append(head.val)
        head = head.next

    out = []
    while stack:
        out.append(stack.pop())
    return out
