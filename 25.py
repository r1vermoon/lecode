'''
回文链表
给你一个单链表的头节点 head ，
请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
'''
class Solution(object):
    def middleNode(self,head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

    def reverselist(self,head):
        cur=head
        pre=None
        while cur:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        return pre

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        mid=self.middleNode(head)
        head2=self.reverselist(mid)
        while head2:
            if head.val!=head2.val:
                return False
            head=head.next
            head2=head2.next
        return True
        