'''
最长回文子字符串

Manacher(马拉车)算法
http://blog.csdn.net/dyx404514/article/details/42061017

快60%左右
'''


def match_both_sides(n, len_n, middle, start=1):
    right_res = []
    left_step, rigt_step = middle - start, middle + start
    while left_step >= 0 and rigt_step < len_n:
        if n[left_step] != n[rigt_step]:
            break
        right_res.append(n[rigt_step])
        rigt_step += 1
        left_step -= 1
    return rigt_step - 1, right_res


def longest_palindromic_substring(n):
    n = n.strip()
    len_n = len(n)
    if not n or len_n == 1:
        return n
    longest_right = []
    new_str = '#' + '#'.join(list(n)) + '#'
    res = []
    mx = 0
    p = 0
    index = 0
    len_n = 2 + (len_n * 2 - 1)
    count = 0
    parent_right_res = []
    while index < len_n:
        if index >= mx:
            right_index, right_res = match_both_sides(new_str, len_n, index)
            max_len = len(right_res)
            res.append(max_len)
            if max_len > count:
                parent_right_res = right_res
                count = max_len
                longest_right = list(reversed(right_res)) + [new_str[index]] + right_res
                mx = right_index
                p = index
        else:
            # index的关于p的对称点
            j = p - (index - p)
            if res[j] >= mx - index:
                # 这里的match如果偷懒的话也可以从index开始向两边匹配，但是这样并不好，没有达到只匹配未匹配的字符串的目的，这样就跟n^2算法就一样了
                # 因此, 这里如果不从mx之后的字符开始匹配的话, leetcode会超时
                right_index, right_res = match_both_sides(new_str, len_n, index, mx - index + 1)
                max_len = len(right_res) + (mx - index)
                res.append(max_len)
                if max_len > count:
                    right_res = parent_right_res[index - p:] + right_res
                    parent_right_res = right_res
                    count = max_len
                    longest_right = list(reversed(right_res)) + [new_str[index]] + right_res
                    mx = right_index
                    p = index
            else:
                res.append(res[j])
        index += 1
    longest_right = ''.join([_ for _ in longest_right if _ != '#'])
    return longest_right


def main():
    strs = ['aaaa12', 'babad', 'aaa', 'aaaba', 'aaaa1a',
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"]
    for s in strs:
        print(s, longest_palindromic_substring(s))
    return


if __name__ == '__main__':
    main()
