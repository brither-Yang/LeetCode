'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
自底向上归并
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def sortList(self, head):

        h, length, intv = head, 0, 1

        while h:
            h, length = h.next, length + 1

        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next

            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break  # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = intv, intv - i  # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next

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
    newHead = ss.sortList(head)
    ss.printLink(newHead)