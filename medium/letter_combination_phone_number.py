'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
'''


def merge(a, b):
    res = []
    for i in a:
        for j in b:
            res.append('%s%s' % (i, j))
    return res


def lcpn(s):
    number_dict = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz',
                   }
    strs = []
    res = []
    for sub in s:
        sub_num = number_dict[sub]
        strs.append((sub_num, len(sub_num)))
    return


def main():
    ss = ['23']
    for s in ss:
        print(lcpn(s))
    return


if __name__ == '__main__':
    main()
