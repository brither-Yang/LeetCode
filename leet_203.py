class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():

    def removeElements(self, head, val):

        if head is None:
            return None

        dummy = tem = ListNode(-1)

        cur = head
        while cur:
            if cur.val == val:
                cur = cur.next
            else:
                tem.next = cur
                tem = tem.next
                cur = cur.next
        tem.next = None
        return dummy.next

        # new_head = tem = ListNode(-1)
        # cur = head
        # while cur:
        #     if cur.val == val:
        #         cur = cur.next
        #         tem.next = cur
        #     else:
        #         tem.next = cur
        #         tem = tem.next
        #         cur = tem.next
        # return new_head.next

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
head = ss.creatLink([1, 2, 6, 3, 4, 5, 6])
ss.printLink(head)
new_head = ss.removeElements(head, 6)
ss.printLink(new_head)