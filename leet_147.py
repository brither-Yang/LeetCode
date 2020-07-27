'''
对链表进行插入排序
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):

        # dummy = ListNode(-1)
        # pre = dummy
        # cur = head
        #
        # while cur:
        #     tmp = cur.next
        #     while pre.next and pre.next.val < cur.val:
        #         pre = pre.next
        #
        #     cur.next = pre.next
        #     pre.next = cur
        #     pre = dummy
        #     cur = tmp
        # return dummy.next

        dummy = ListNode(-1)
        pre = dummy

        cur = head
        while cur:
            tem = cur.next

            while pre.next and cur.val < tem.val:
                pre = pre.next

            cur.next = pre.next
            pre.next = cur
            pre = dummy
            cur = tem

        return dummy.next


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


if __name__ == '__main__':
    ss = Solution()
    head = ss.creatLink([3, 6, 5, 8, 7, 1, 2, 4])
    ss.printLink(head)
    newHead = ss.insertionSortList(head)
    ss.printLink(newHead)