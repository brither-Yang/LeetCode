'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定 nums = [1,1,1,2,2,3],

函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,1,2,3,3],

函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

你不需要考虑数组中超出新长度后面的元素。

'''

class ListNode():

    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():

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

    def partition(self, head, x):

        if not head:
            return None

        # head1 为小于 x 的链表头节点
        # head2 为大于 x 的链表头节点
        # head1 的尾节点连接 head2 的头节点
        head1 = tem1 = ListNode(-1)
        head2 = tem2 = ListNode(-1)

        cur = head
        while cur:
            if cur.val > x:
                tem2.next = cur
                tem2 = tem2.next
            else:
                tem1.next = cur
                tem1 = tem1.next
            cur = cur.next
        tem1.next = head2.next

        return head1.next


if __name__ == '__main__':
    array = [1, 2, 4, 2, 3, 5, 6]
    ss = Solution()
    head = ss.creatLink(array)
    ss.printLink(head)
    newHead = ss.partition(head, 3)
    ss.printLink(newHead)
