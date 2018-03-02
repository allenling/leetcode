'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

想法是O(n)

第一次才领先14%~~~尴尬

应该是在遇到重复的时候不应该回位置那么多的, 比如dvadfw:

遇到第二个d的时候, 直接从v开始, 可以直接从d开始, 字典初始化为{v, d}

操作就是把dict中的d的位置更新一下, 然后current_start从重复的d后面一位开始, 然后更新current_len = i - current_start + 1

然后继续遍历就好了, 这样就是O(n)了, 不需要重新从重复字符的后面以为开始遍历, 必须上面的例子, 不需要从dvad的第一个d后面的v开始遍历

更新d的位置为3后, 更新current_start = 1, current_len = 3 - 1 + 1 = 3, 然后继续从第二个d开始遍历就好了

并且如果发现重复的, 但是位置小于current_start的, 可以直接更新就好

第二次是领先36%, 差不多感觉

'''


def lswr(s):
    if not s:
        return ''
    len_s = len(s)
    if len_s == 1:
        return s
    current_start = max_start = 0
    i = current_len = max_len = 0
    sub_dict = {}
    while i < len_s:
        current = s[i]
        if current not in sub_dict or sub_dict[current] < current_start:
            current_len += 1
            sub_dict[current] = i
        else:
            if current_len > max_len:
                max_start = current_start
                max_len = current_len
            current_start = sub_dict[current] + 1
            current_len = i - current_start + 1
            sub_dict[current] = i
        i += 1
    if current_len > max_len:
        max_start = current_start
        max_len = current_len
    return s[max_start: max_start + max_len]


def main():
    ss = ['abba', 'dvdf', 'au', 'pwwkew', 'abcabcbb', 'bbbbb']
    for s in ss:
        print(s, lswr(s))
    return


if __name__ == '__main__':
    main()
