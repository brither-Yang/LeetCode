class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def isPalindrome(self, head: ListNode) -> bool:

        def reverseLink(head):

            if not head:
                return head

            pre = None
            cur = head

            while cur:
                nex = cur.next

                cur.next = pre
                pre = cur
                cur = nex

            return pre

        if not head:
            return True

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        newHead = reverseLink(head2)

        cur1 = head1
        cur2 = newHead
        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next

        return True

    def creatLink(self, array):

        head = ListNode(-1)
        cur = head
        for i in range(len(array)):
            node = ListNode(array[i])
            cur.next = node
            cur = cur.next
        return head.next

    def printLink(self, head):

        tem = head
        while tem:
            print(tem.val, end=' -> ')
            tem = tem.next
        print('None')


ss = Solution()
head = ss.creatLink([1, 2, 3, 2, 1])
ss.printLink(head)
print(ss.isPalindrome(head))
