'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

动态规划, 遍历一次, 使用中间变量保存结果, O(n)

第一次才领先14%~~~尴尬

第二次是领先36%, 差不多感觉

2018-06-02再修改, 想了一个流程, 然后自己也看不懂了, 然后过了leetcode, 领先83.55%, 耗时88ms

最快68ms, 我这里中间变量用得多, 耗时多一点点, 思路差不多
'''


def lswr(word):
    '''
    判断2部分, 也就是调整下面两部分的下标:
    abcde bfgh
    1. abcde
    2. cdebfgh

    下面的流程, 虽然是我自己想出来的, 但是我自己都看不懂了
    '''
    word_len = len(word)
    if not word:
        return 0
    if word_len == 1:
        return 1
    if word_len == 2:
        return 1 if word[0] == word[1] else 2
    max_dict = {}
    max_start = max_end = 0
    split_index = None
    for index, w in enumerate(word):
        w = word[index]
        old_index = max_dict.get(w, None)
        max_dict[w] = index
        if split_index is not None:
            if old_index is None or old_index < split_index:
                continue
            else:
                last_len = index - split_index
                if last_len >= (max_end - max_start + 1):
                    max_start, max_end = split_index, index - 1
                    split_index = old_index + 1
                else:
                    split_index = old_index + 1
        else:
            if old_index is None:
                max_end = index
            else:
                split_index = old_index + 1
    # finally
    max_len = (max_end - max_start + 1)
    if split_index is not None:
        max_len = max(max_len, word_len - split_index)
    return max_len


def main():
    ss = ['bpoiexpqhmebhhu', 'pwwkew', 'abba', 'dvdf', 'au', 'abcabcbb', 'bbbbb']
    for s in ss:
        print(s, lswr(s))
    print('-----------------')
    for s in ss:
        print(s, lswr(s))
    return


if __name__ == '__main__':
    main()
