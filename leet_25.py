'''
25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5



说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def reverse(head, tail):
            # 反转一个子链表，返回反转后的头与尾
            pre = tail.next
            p = head
            while pre != tail:
                nex = p.next
                p.next = pre
                pre = p
                p = nex
            return tail, head

        dummy = ListNode(0)
        dummy.next = head
        first = last = dummy

        while last:
            tail = first
            # 查看剩余部分是否小于 k
            for i in range(k):
                if not tail:
                    return dummy.next
                tail = tail.next
                pre, tail = reverse(first, tail)
                # 把子链表重新接回原链表
                first.next =
                tail.next = nex
                pre = tail
                head = tail.next

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
newHead = ss.reverseKGroup(head, 3)
ss.printLink(newHead)