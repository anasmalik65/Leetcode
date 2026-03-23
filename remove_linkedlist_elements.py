
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        prev, curr = temp, head
        while curr:
            if curr.val == val:prev.next = curr.next
            else:prev = curr
            curr = curr.next
        return temp.next
        