'''
https://leetcode.com/problems/word-search/description/

一开始是做list的hash表, 复杂度O(MN), leetcode超时

其他解决方法是dfs, 深度优先搜索~~~~~但是dfs的话是要一个个搜索的, 最坏情况也是mn呀

还有字典树, 感觉字典树也不靠谱呀: https://segmentfault.com/a/1190000003697153
'''


def search_word(nlist, row_count, col_count, row, col, pre_row, pre_col, w):
    '''
    从row, col这个点开始, 四个方向搜索单词w
    成功返回(next_row, next_col)
    失败返回-1
    '''
    got_it = False
    next_row = next_col = None
    # 四个方向
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    # 有效的方向
    next_directions = [(row + i, col + j) for i, j in directions if row_count > row + i >= 0 and col_count > col + j >= 0]
    for next_row, next_col in next_directions:
        if next_row == pre_row and next_col == pre_col:
            continue
        if nlist[next_row][next_col] == w:
            got_it = True
            break
    if got_it is True:
        return (next_row, next_col)
    return -1


def word_search(nlist, w):
    res = False
    start_points = {}
    len_nlist = len(nlist)
    cl_count = len(nlist[0])
    row = 0
    col_count = len(nlist[0])
    while row < len_nlist:
        col = 0
        while col < col_count:
            v = nlist[row][col]
            if v not in start_points:
                start_points[v] = [(row, col)]
            else:
                start_points[v].append((row, col))
            col += 1
        row += 1
    w_count = 0
    start = w[w_count]
    len_w = len(w)
    if start in start_points:
        for row, col in start_points[start]:
            # 每一个起始点开始搜索
            s_res = None
            pre_row, pre_col = -1, -1
            w_count = 1
            while w_count < len_w:
                s_res = search_word(nlist, len_nlist, cl_count, row, col, pre_row, pre_col, w[w_count])
                if s_res == -1:
                    break
                w_count += 1
                pre_row, pre_col = row, col
                row, col = s_res
            if s_res != -1:
                res = True
                break
    return res


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        if len(board) == 1:
            if len(word) == 1:
                return word in board[0]
            tmp = ''.join(board[0])
            return tmp == word
        if len(word) == 1:
            for i in board:
                if word in i:
                    return True
            return False
        res = word_search(board, word)
        return res


def main():
    s_pa = [['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E'],
            ]
    ws = ['ABCB', 'ABCCED', 'SEE']
    s = Solution()
    print(s.exist([['a', 'a']], 'a'))
    for w in ws:
        print(word_search(s_pa, w))
    return


if __name__ == '__main__':
    main()
