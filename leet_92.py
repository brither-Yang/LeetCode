'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''
class ListNode():

    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():

    def creatLink(self, array):

        dummy = tem = ListNode(-1)

        for i in array:
            node = ListNode(i)
            tem.next = node
            tem = tem.next

        return dummy.next

    def printLink(self, head):

        cur = head

        while cur:
            print(cur.val, end=' -> ')
            cur = cur.next
        print('None')

    def reverseBetween(self, head, m, n):

        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # 存储第一段链表的尾节点
        tem = dummy
        for i in range(m-1):
            tem = tem.next

        # 反转 m -> n 之间的链表
        # cur 为第二段头节点
        # p 为第三段头节点
        # pre 为第二段反转后的新头节点
        pre = None
        cur = p = tem.next

        for i in range(m, n+1):
            nex = p.next

            p.next = pre
            pre = p
            p = nex

        tem.next = pre
        cur.next = p

        return dummy.next


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6]
    ss = Solution()
    head = ss.creatLink(array)
    ss.printLink(head)
    newHead = ss.reverseBetween(head, 1, 6)
    ss.printLink(newHead)

    dummy = tem = ListNode(-1)
    dummy.next = head

