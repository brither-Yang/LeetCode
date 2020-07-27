class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():

    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        cur = l1
        while cur:
            stack1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            stack2.append(cur.val)
            cur = cur.next

        num1, num2 = 0, 0
        i, j = 0, 0
        while stack1:
            num1 += stack1.pop() * 10 ** i
            i += 1
        while stack2:
            num2 += stack2.pop() * 10 ** j
            j += 1
        num = num1 + num2
        numStr = str(num)

        head = tem = ListNode(int(numStr[0]))
        for i in numStr[1:]:
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
head1 = ss.creatLink([7, 2, 4, 3])
head2 = ss.creatLink([5, 6, 4])
head = ss.addTwoNumbers(head1, head2)
ss.printLink(head)
