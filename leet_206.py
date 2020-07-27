'''
反转一个单链表
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

    def reverseList(self, head):

        pre = None
        cur = head

        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6]
    ss = Solution()
    head = ss.creatLink(array)
    ss.printLink(head)
    newhead = ss.reverseList(head)
    ss.printLink(newhead)


