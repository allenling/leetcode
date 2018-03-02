'''
只快了50%左右, 尽量避免无所谓的判断, 以及while的时候如果能直接判断退出就不要等到下一个循环再判断
'''

# Definition for singly-linked list.
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        if head.next is None:
            return head
        parent = head
        grad = res = ListNode(None)
        while True:
            child = parent.next
            parent.next, child.next = child.next, parent
            grad.next = child
            grad = parent
            parent = parent.next
            if parent is None or parent.next is None:
                break
        return res.next


def stringToIntegerList(i):
    return json.loads(i)


def stringToListNode(i):
    # Generate list from the input
    numbers = stringToIntegerList(i)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    v = '''[1,2,3,4]'''

    def readlines():
        for line in v.splitlines():
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line)

            ret = Solution().swapPairs(head)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
