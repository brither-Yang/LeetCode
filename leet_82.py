'''
82. 删除排序链表中的重复元素 II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
'''


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():

    def deleteDuplicates(self, head):

        if not head or not head.next:
            return head

        slow = dummy = ListNode(None)

        fast = head
        while fast:
            if fast.next and fast.next.val == fast.val:
                tem = fast.val
                while fast and fast.val == tem:
                    fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next
        slow.next = fast

        return dummy.next

        # if head.next and head.val == head.next.val:
        #     while head.next is not None and head.val == head.next.val:
        #         head = head.next
        #     return self.deleteDuplicates(head.next)
        # else:
        #     head.next = self.deleteDuplicates(head.next)
        # return head

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
head = ss.creatLink([1, 1, 2, 3, 4, 4, 4, 5, 6])
ss.printLink(head)
head1 = ss.deleteDuplicates(head)
ss.printLink((head1))
