class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or pHead.next:
            return pHead

        cur = pHead
        nex = pHead.next

        while nex:
            if cur.val == nex.val:
                nex = nex.next
            else:
                cur.next = nex
                cur = nex
                nex = nex.next
        return pHead

    def creatLink(self, array):

        head = tem = ListNode(array[0])
        for i in array[1:]:
            node = ListNode(array[i])
            tem.next = node
            tem = tem.next
        return head

    def travelLink(self, head):
        if not head:
            print(None)
            return

        tem = head
        while tem:
            print(tem.val, end=' -> ')
            tem = tem.next
        print('None')

ss = Solution()
head = ss.creatLink([1, 1, 2, 2, 3, 5, 6])
ss.travelLink(head)
newHead = ss.deleteDuplication(head)
ss.travelLink(newHead)