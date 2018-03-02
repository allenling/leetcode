'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

遍历的时候用dict记录下对应位置的node
快于37%
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return 'ListNode: %s' % self.val

    def __repr__(self):
        return self.__str__()


def rnfe(root, n):
    if root.next is None:
        return None
    node_dict = {}
    index = 0
    node = root
    while node is not None:
        node_dict[index] = node
        node = node.next
        index += 1
    index -= 1
    i = index - n + 1
    if i == 0:
        root = node_dict[1]
    else:
        pre_node = node_dict[i - 1]
        if i == index:
            next_node = None
        else:
            next_node = node_dict[i + 1]
        pre_node.next = next_node
    return root


def get_node_from_list(nlist):
    root = ListNode(nlist[0])
    node = root
    for v in nlist[1:]:
        next_node = ListNode(v)
        node.next = next_node
        node = next_node
    return root


def get_list_from_node(root):
    if root is None:
        return []
    node = root
    res = []
    while node is not None:
        res.append(node.val)
        node = node.next
    return res


def main():
    ss = []
    for i in range(1, 6):
        ss.append([get_node_from_list(list(range(1, 6))), i])
    ss.insert(0, [ListNode(1), 1])
    for root, n in ss:
        new_root = rnfe(root, n)
        print(n, get_list_from_node(new_root))
    return


if __name__ == '__main__':
    main()
