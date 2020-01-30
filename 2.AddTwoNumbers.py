# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
# reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked
# list.

class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


class Solution(object):
    def addTwoNumbers(self, List1, List2):
        """Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        Parameters
        ----------
            L1: `List[int]`
            L2: int
        Returns
        -------
            Index of two numbers.
        """
        LL1 = LinkedList()
        for i, num in enumerate(List1):
            LL1.append(ListNode(num))
        LL2 = LinkedList()
        for i, num in enumerate(List2):
            LL2.append(ListNode(num))
        



L1 = [2, 4, 3]
L2 = [5, 6, 4]
a = Solution()
a.setupList(L1)
