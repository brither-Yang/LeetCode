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

    def deleteDuplicates(self, head):

        if not head:
            return head

        # 以 head 开始遍历链表
        # cur 为当前节点，nex 为下一个节点
        # 当 cur 与 nex 的值不相等时，cur.next = nex
        # 否则 cur 不变，nex 继续遍历

        cur = head
        nex = cur.next

        while nex:
            if cur.val == nex.val:
                nex = nex.next
            else:
                cur.next = nex
                cur = cur.next
                nex = nex.next
        cur.next = nex
        return head


        # if not head:
        #     return None
        #
        # cur = head
        # tem = cur.next
        #
        # while tem:
        #     val1 = cur.val
        #     val2 = tem.val
        #
        #     if val1 == val2:
        #         tem = tem.next
        #     else:
        #         cur.next = tem
        #         cur = cur.next
        #         tem = cur.next
        # cur.next = None
        # return head


if __name__ == '__main__':
    array = [1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 6]
    ss = Solution()
    head = ss.creatLink(array)
    ss.printLink(head)
    newHead = ss.deleteDuplicates(head)
    ss.printLink(newHead)
