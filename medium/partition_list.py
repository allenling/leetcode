'''
https://leetcode.com/problems/partition-list/description/

给出: 1->4->3->2->5->2 and x = 3,
输出: 1->2->2->4->3->5.

小于3的节点放到前面, 大于3的节点顺序不变

leetcode上显示, 我是最快的!!!!!快于100%
'''
import itertools


class ListNode:
    def __init__(self, v, next_node=None):
        self.val = v
        self.next = next_node

    def __str__(self):
        return '%s' % self.val

    def __repr__(self):
        return self.__str__()


def gen_linked_list(it):
    prev = root = ListNode(it[0])
    for i in it[1:]:
        n = ListNode(i)
        prev.next = n
        prev = n
    return root


def iter_root(root):
    res = []
    node = root
    while True:
        res.append('%s' % node.val)
        if node.next is None:
            break
        node = node.next
    res = '->'.join(res)
    return res


def partition_list(root, n):
    if not root or root.next is None:
        return root
    # !注意root是大于等于n的情况!
    current_node = prev_node = root
    greater_nodes = []
    less_nodes = []
    while True:
        if current_node.val >= n:
            prev_node.next = current_node.next
            greater_nodes.append(current_node)
        else:
            less_nodes.append(current_node)
            prev_node = current_node
        current_node = current_node.next
        if current_node is None:
            break
    # combine two linked list
    prev_node = root = ListNode(None)
    for i in itertools.chain(less_nodes, greater_nodes):
        prev_node.next = i
        prev_node = i
    prev_node.next = None
    root = root.next
    return root


def main():
    datas = [([1, 4, 3, 2, 5, 2], 3),
             ]
    for data in datas:
        it, v = data
        root = gen_linked_list(it)
        print('before: %s' % iter_root(root))
        partition_list(root, v)
        print('after: %s' % iter_root(root))
    return


if __name__ == '__main__':
    main()
