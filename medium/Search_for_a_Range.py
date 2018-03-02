'''
https://leetcode.com/problems/search-for-a-range/description/

快39%

感觉在边界条件上可以多判断一下, 避免二分的次数
'''


def binary_search(nlist, start, end, v, pos=None):
    res = -1
    while True:
        if abs(end - start) == 1 or end == start:
            if nlist[start] == nlist[end] == v:
                if pos == 'left':
                    res = start
                else:
                    res = end
            elif nlist[start] == v:
                res = start
            elif nlist[end] == v:
                res = end
            break
        mid = int((end - start) / 2) + start
        if nlist[mid] == v:
            res = mid
            break
        elif nlist[mid] > v:
            end = mid
        else:
            start = mid
    return res


def sfar(nlist, v):
    res = [-1, -1]
    if not nlist:
        return res
    len_l = len(nlist)
    if len_l == 1:
        if nlist[0] == v:
            return [0, 0]
        else:
            return res
    # 下面是二分
    mid = binary_search(nlist, 0, len_l - 1, v)
    if mid == -1:
        return res
    left_index = right_index = mid
    if mid != 0:
        start, end = 0, mid - 1
        while True:
            last_index = binary_search(nlist, start, end, v, pos='left')
            if last_index != -1:
                left_index = last_index
                if end == left_index or left_index <= 0:
                    break
                end = left_index - 1
                continue
            break
    else:
        left_index = 0
    left_index = left_index if left_index != -1 and left_index < mid else mid
    if mid != len_l - 1:
        start, end = mid + 1, len_l - 1
        while True:
            last_index = binary_search(nlist, start, end, v, pos='right')
            if last_index != -1:
                right_index = last_index
                if start == right_index or right_index >= len_l - 1:
                    break
                start = right_index + 1
                continue
            break
        right_index = right_index if right_index != -1 and right_index > mid else mid
    else:
        right_index = mid
    return [left_index, right_index]


def main():
    t = [[[1, 2, 5, 5, 5, 6, 7, 8, 9, 10], 5],
         [[1, 2, 2, 3, 4, 4, 4], 4],
         [[5, 5, 5, 5, 5, 5, 5, 8, 9, 10], 10],
         [[5, 7, 7, 8, 8, 10], 8],
         [[1, 2, 5, 5, 5, 5, 7, 8, 9, 10], 5],
         [[5, 5, 5, 5, 5, 5, 5, 8, 9, 10], 5],
         [[5, 5, 5, 5, 5, 5, 5, 8, 9, 10], 9],
         [[1], 1],
         [[1], 0],
         ]
    for l, s in t:
        print(l, s, sfar(l, s))
    return


if __name__ == '__main__':
    main()
