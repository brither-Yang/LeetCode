'''
234. 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reorderList(self, head):

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

        if not head or not head.next:
            return head

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        newHead = reverseLink(head2)

        dummy = tem = ListNode(-1)
        p = 0
        cur1 = head1
        cur2 = newHead
        while cur1 and cur2:
            if p % 2 == 0:
                tem.next = cur1
                cur1 = cur1.next
            else:
                tem.next = cur2
                cur2 = cur2.next
            tem = tem.next
            p += 1
        tem.next = cur1

        return dummy.next

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
head = ss.creatLink([1, 2, 3, 4, 5, 6, 7, 8, 9])
ss.printLink(head)
head1 = ss.reorderList(head)
ss.printLink(head1)
