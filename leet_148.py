'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def sortList(self, head):

        # termination
        if not head or not head.next:
            return head

        # cut the LinkedList at the mid index.
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None  # save and cut.

        # recursive for cutting.
        left = self.sortList(head)
        right = self.sortList(mid)

        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next

            else:
                h.next = right
                right = right.next

            h = h.next
        h.next = left if left else right
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