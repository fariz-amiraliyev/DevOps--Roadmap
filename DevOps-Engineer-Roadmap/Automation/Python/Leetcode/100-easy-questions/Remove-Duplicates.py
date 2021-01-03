Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        if not head:
            return None
        while head != None:
            arr.append(head.val)
            head = head.next

        li = []
        for i in arr:
            if i not in li:
                li.append(i)

        node = ListNode(li[0])
        head = node

        for i in range(1,len(li)):
            node.next = ListNode(li[i])
            node = node.next

        return head
