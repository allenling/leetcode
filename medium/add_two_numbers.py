'''
没看答案
快于69%左右
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        plus = 0
        res = []
        while True:
            if l1 is None and l2 is None:
                if plus:
                    res.append(ListNode(plus))
                break
            sum_res = 0 if not l1 else l1.val
            sum_res += 0 if not l2 else l2.val
            sum_res += plus
            plus, num = sum_res // 10, sum_res % 10
            res.append(ListNode(num))
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        res.reverse()
        count = 1
        while count < len(res):
            res[count].next = res[count - 1]
            count += 1
        return res[-1]


def main():
    return


if __name__ == '__main__':
    main()
