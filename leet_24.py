'''
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
'''


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def swapPairs(self, head):

        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head
        p = dummy

        while p and p.next and p.next.next:
            node1 = p.next
            node2 = p.next.next
            nex = p.next.next.next

            p.next = node2
            node2.next = node1
            node1.next = nex
            p = node1
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
head = ss.creatLink([1, 2, 3, 4, 5, 6, 7])
ss.printLink(head)
newHead = ss.swapPairs(head)
ss.printLink(newHead)
