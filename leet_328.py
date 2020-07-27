class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():

    def oddEvenList(self, head):

        odd = head
        even_head = even = head.next

        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            even, odd = even.next, odd.next
        odd.next = even_head
        return head

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
head = ss.creatLink([1, 2, 3, 4, 5, 6])
ss.printLink(head)
new_head = ss.oddEvenList(head)
ss.printLink(new_head)
