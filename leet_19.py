class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():

    def removeNthFromEnd(self, head, n):

        if not head or not head.next:
            return head

        tem = head
        for i in range(n-1):
            tem = tem.next

        cur = dummy = ListNode(-1)
        cur.next = head
        while tem.next:
            tem = tem.next
            cur = cur.next

        cur.next = cur.next.next
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
head = ss.creatLink([1, 2, 3, 4, 5])
ss.printLink(head)
newHead = ss.removeNthFromEnd(head, 5)
ss.printLink(newHead)
