# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        count=0
        n=0
        while t:
            n+=1
            t=t.next
        if n==1:
            head=None
            del t
            return head
        t=head
        while t:
            if count==((n//2)-1):
                p=t.next
                t.next=p.next
                del p
                break
            t=t.next
            count+=1
        return head