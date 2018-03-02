'''
验证二叉搜索树

判断子树是否满足left < node < right这样是不行, 因为left, right和parent_node不一定满足二叉搜索树的性质,
判断起来很复杂

比如这个子树300, 100, None, 300 > 100满足条件
然后100这个子树, 有100, None, 150, 有150 > 100, 满足条件
然后150这个子树，有150, 90, None, 有150 > 90，满足条件，但是90 < 100, 90应该是100的左子树
如果150这个子树，满足条件，假设为150, 120, 180, 有180>150>120, 然后你无法保证120的子树也满足150 > 120_left > 100
比如120这个子树，有120,90,None, 这样也不满足二叉搜索树的性质了，因为90<100, 应该是100的左子树

这个判断太复杂了

其实可以这样
构建新的二叉搜索树, 然后比较输入和新的树, 或者按照二叉搜索树的查找方法查找每一个节点，判断位置是否正确, 判断条件就是
如果没有搜索到就是False, 搜索到了就是True, 但是注意的是这样情况1, None, 1, 这种情况搜索1的时候是能搜索到的, 但是位置不对,
要加入一个位置判断, 可以直接判断, 判断parent, node, left, right是否和原树一致
nlog2n, 每个节点都遍历一次, 就是n, 每次搜索是log2n, 所以是nlog2n, 最坏的情况，也就是树退化成线性的，这个时候搜索也是n, 所以是n*n
快于2.3%左右~~好尴尬

如何降到n?
好多人都说可以中序遍历之后判断是否有序，但是中序遍历一次是n, 然后判断是否有序也是n, 不就是n*n了吗， 好吧，好像是遍历的时候记住最大值和最小值，判断是否
小于最小值或者大于最大值
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def search(self, root, val, parent, left, right):
        vs = [parent.val, left.val if left else None, right.val if right else None]
        is_in = False
        nodes = [root]
        tmp_parent = None
        while nodes:
            node = nodes.pop(0)
            if node.val == val:
                tmp_vs = [(tmp_parent.val if tmp_parent else None) == vs[0],
                          (node.left.val if node.left else None) == vs[1],
                          (node.right.val if node.right else None) == vs[2],
                          ]
                if all(tmp_vs):
                    is_in = True
                break
            tmp_parent = node
            if node.val > val and node.left:
                nodes.append(node.left)
            elif node.val < val and node.right:
                nodes.append(node.right)
        return is_in

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        ns = [(root.left, root), (root.right, root)]
        while ns:
            node, parent = ns.pop(0)
            if not node:
                continue
            val = node.val
            is_right = self.search(root, val, parent, node.left, node.right)
            if is_right is False:
                return False
            ns.extend([(node.left, node), (node.right, node)])
        return True


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    inv = '''[100, 50, 150, 42, 60, 120, 180]
    [100, 50, 150, 42, 60, 120]
    [100, 50, 150, 42, 60]
    []
    [1,2,3]
    [3,2,1]
    [2,1,3]
    [1,null,1]
    [10,5,15,null,null,6,20]
    [3,1,5,0,2,4,6,null,null,null,3]'''
    def readlines():
        for line in inv.splitlines():
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines).strip()
#             print(line)
#             line = '''[1,null,1]'''
            root = stringToTreeNode(line);
            ret = Solution().isValidBST(root)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()