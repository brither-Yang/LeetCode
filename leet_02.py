class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():

    def addTwoNumbers(self, l1, l2):

        num1 = 0
        num2 = 0
        cur = l1
        k = 0
        while cur:
            num1 += cur.val * 10 ** k
            k += 1
            cur = cur.next

        cur = l2
        j = 0
        while cur:
            num2 += cur.val * 10 ** j
            j += 1
            cur = cur.next

        num = str(num1 + num2)[::-1]
        head = tem = ListNode(int(num[0]))
        for i in num[1:]:
            node = ListNode(int(i))
            tem.next = node
            tem = tem.next

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
head1 = ss.creatLink([1, 8, 3])
ss.printLink(head1)
head2 = ss.creatLink([4, 7, 3])
ss.printLink(head2)
new_head = ss.addTwoNumbers(head1, head2)
ss.printLink(new_head)