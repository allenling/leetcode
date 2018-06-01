'''
word search
如果用循环的形式计算四个角度的话, 很耗时间
如果是一个个if判断的话, 比如下面, 就快得多!!!!

最快的版本是递归dfs, 使用了内置函数Counter, 很快, 然后我这里使用了太多中间变量, 导致花了很多时间
非递归版本和递归版本相比, 很多中间变量是不可避免的, 但是这个不是非常多
震惊的是, 一次性计算四个方向消耗很大, 消耗居然在于return列表!!!你敢信

v1: 逐个加入current_path_set的形式替换掉每次都使用set()去生成current_path_set
    get_directions是列表形式计算四个方向
    过leetcode时间是496ms, 然后快于10.57%~~sad

v2: get_directions使用if而不是列表的形式计算四个方向
    过leetcode时间是340ms, 然后快于30.84%~~还可以

'''
from collections import deque

@profile
def get_directions(cor, max_row_index, max_col_index):
    sub_row, sub_cell = cor
    directions = []
    upper = sub_row - 1
    right = sub_cell + 1
    bottom = sub_row + 1
    left = sub_cell - 1
    if 0 <= upper:
        directions.append((upper, sub_cell))
    if right <= max_row_index:
        directions.append((sub_row, right))
    if bottom <= max_col_index:
        directions.append((bottom, sub_cell))
    if 0 <= left:
        directions.append((sub_row, left))
    return directions


def get_first_two_path(cor, board, max_row_index, max_col_index, word):
    walk_deq = deque()
    first_point = None
    directions = get_directions(cor, max_row_index, max_col_index)
    for next_d in directions:
        if board[next_d[0]][next_d[1]] == word[1]:
            first_point = cor
            walk_deq.appendleft([cor, next_d])
    return walk_deq, first_point

@profile
def divide_walk_board(board, word):
    word_len = len(word)
    board_len = len(board)
    row_len = len(board[0])
    max_row_index = row_len - 1
    max_col_index = board_len - 1
    row_index = -1
    for row in board:
        row_index += 1
        cell_index = -1
        for cell in row:
            cell_index += 1
            if cell == word[0]:
                if word_len == 1:
                    return True
                # 开始步进
                walk_deq, first_point = get_first_two_path((row_index, cell_index), board, max_row_index, max_col_index, word)
                if not walk_deq:
                    continue
                if word_len == 2:
                    return True
                current_path_set = set([first_point])
                while walk_deq:
                    current_path = walk_deq.popleft()
                    # too much time!
                    # current_path_set = set(current_path)
                    current_len = len(current_path)
                    last_cor = current_path[-1]
                    current_path_set.add(last_cor)
                    # too much time
                    last_directions = get_directions(last_cor, max_row_index, max_col_index)
                    next_w = word[current_len]
                    # board[i][j], too much time
                    next_valid_direction = [tmp_cor for tmp_cor in last_directions if board[tmp_cor[0]][tmp_cor[1]] == next_w]
                    # keep order
                    next_valid_direction = [i for i in next_valid_direction if i not in current_path_set]
                    if next_valid_direction:
                        if current_len + 1 == word_len:
                            return True
                        for m in next_valid_direction:
                            # too much time!
                            new_path = current_path + [m]
                            walk_deq.appendleft(new_path)
                    else:
                        try:
                            last_path = walk_deq.popleft()
                        except IndexError:
                            break
                        current_path_set = set(last_path)
                        walk_deq.appendleft(last_path)
    return False


def main():
    max_board = [['a'] * 30 for _ in range(29)]
    max_board.append(['a'] * 29 + ['b'])
    max_word = 'b' + 'a' * 899
    res = divide_walk_board(max_board, max_word)
    print('max_board', res)
#     boards = [[["A", "B", "C", "E"],
#                ["S", "F", "E", "S"],
#                ["A", "D", "E", "E"],
#                ],
#               [['a', 'a', 'c'],
#                ['e', 'd', 'q'],
#                ],
#               [['A', 'B', 'E', 'E'],
#                ['S', 'F', 'C', 'S'],
#                ['A', 'D', 'C', 'E'],
#                ],
#               [['a', 'a'],
#                ],
#               [['A', 'B', 'C', 'E'],
#                ['S', 'F', 'C', 'S'],
#                ['A', 'D', 'E', 'E'],
#                ],
#               ]
#     words = [['ABCESEEEFS'], ['aada'], ['SEE', 'ABCCED', 'ABCB'], ['aa'], ['ABCCED', 'ABCCEDFB']]
#     for board, word_list in zip(boards, words):
#         for word in word_list:
#             res = divide_walk_board(board, word)
#             print(word, res)
    return


if __name__ == '__main__':
    main()
