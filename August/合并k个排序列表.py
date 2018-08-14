'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = []
        head = ListNode(0)
        result = head
        for listnode in lists:
            while listnode:
                l.append(listnode.val)
                listnode = listnode.next
        l.sort()
        for i in l:
            head.next = ListNode(i)
            head = head.next
        return result.next

