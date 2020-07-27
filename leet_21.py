class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():

    def mergeTwoLists(self, l1, l2):

        newHead = tem = ListNode(None)
        tem1 = l1
        tem2 = l2

        while tem1 and tem2:
            if tem1.val > tem2.val:
                node = ListNode(tem2.val)
                tem.next = node
                tem2 = tem2.next
            else:
                node = ListNode(tem1.val)
                tem.next = node
                tem1 = tem1.next
            tem = tem.next

        if tem1:
            tem.next = tem1
        if tem2:
            tem.next = tem2
        return newHead.next

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
head1 = ss.creatLink([1, 3, 5, 7, 9])
head2 = ss.creatLink((2, 4, 6, 8))
ss.printLink(head1)
ss.printLink(head2)
head = ss.mergeTwoLists(head1, head2)
ss.printLink(head)

