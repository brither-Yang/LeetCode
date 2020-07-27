class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():

    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        ss = k % n
        if ss == 0:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        p = q = dummy
        for i in range(ss):
            p = p.next

        while p.next:
            p = p.next
            q = q.next
        new_head = q.next
        q.next = p.next
        p.next = dummy.next
        return new_head

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
newHead = ss.rotateRight(head, 7)
ss.printLink(newHead)
