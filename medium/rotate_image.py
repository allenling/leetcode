'''
https://leetcode.com/problems/rotate-image/description/

[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

这个没做完, 先放着!!!!

'''


def diagonal_move(nlist, start_point, end_point, move_setp):
    '''
    '''
    return


def rotate_image(nlist):
    len_n = len(nlist)
    last_sub = len_n - 1
    i = 0
    while i < int(len_n / 2):
        current_columns = len_n - 2 * i
        move_setp = current_columns - 1
        start_point, end_point = [0 + i, 0 + i], [last_sub - i, last_sub - i]
        diagonal_move(nlist, start_point, end_point, move_setp)
        i += 1
    return


def main():
    ss = [[[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ],
          [[5, 1, 9, 11],
           [2, 4, 8, 10],
           [13, 3, 6, 7],
           [15, 14, 12, 16]
           ],
          ]
    for s in ss:
        rotate_image(s)
        for i in s:
            print(i)
        print('--------------')
    return


if __name__ == '__main__':
    main()
