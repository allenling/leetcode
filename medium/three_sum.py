'''
所有三个数相加为0的组合
S = [-1, 0, 1, 2, -1, -4],
[-1, 0, 1],
[-1, -1, 2]

感觉只能遍历所有的情况
这里的思路是: 如果两个数字加起来为n, 那么在S中是否存在一个值x，有x + n =0, x = -n, 快速判断的话就是x是否存在于S中，也就是把所有元素做个字典就可以快速判断了
找出所有三三组合，可以去掉一些重复组合, 比如2, -1, -1和-1, -1 , 2

leetcode上2sum的条件，一个元素只能用一次, leetcode的3sum是元素可以用多次，只是需要去重, 但是花的时间老是超过规定时间, 感觉主要是因为
leetcode的输出是有序的，别人是排序好之后再遍历，我这里是不排序的, 只是对结果排序，但是按理说对结果排序比起对原数组排序快的，因为结果比原数组小呀.

单纯的迭代大list花了250ms
在逻辑判断上: Counter花了6ms, f = sorted([first_v, i, t])花了40多ms, 最后的sorted倒是没花什么时间
倒是in m这个逻辑判断花了500ms, 因为m之前是用Counter的，换成dict之后，减少了500ms, 你敢信
但是还是花了500ms, in m这个逻辑依然会花300+-100ms

把(t == i or t == first_v) and m[t] < 2和t == i == t == first_v and m[t] < 3移到t in m判断之后，时间减少了一点(100ms-200ms),
然后先判断t == i == t == first_v再判断(t == i or t == first_v), 时间减少了一点(100ms)
用for 替代while len < len(n), 时间又减少了一点(100ms-200ms)

第二个循序中加了个if判断之后，就算是用map做O(1)判断，差距也有500ms~~只快了9.3%~~~悲剧, leetcode上780ms就能到前25%, 这个过测试花了1782ms~~~

别人的总结，k-sum问题的复杂度为O(n^(k-1)): http://blog.csdn.net/nanjunxiao/article/details/12524405
'''
#                 # 下面是一个元素只能用一次的逻辑
#                 if t in m:
#                     m[t]['count'] -= 1
#                     m[i]['count'] -= 1
#                     m[first_v]['count'] -= 1
#                     if not all([m[t]['count'] >= 0, m[i]['count'] >= 0, m[first_v]['count'] >= 0]):
#                         m[t]['count'] += 1
#                         m[i]['count'] += 1
#                         m[first_v]['count'] += 1
#                         index += 1
#                         continue
#                     res.append([first_v, i, t])
#                     m[t]['paths'].pop(0)
#                     m[first_v]['paths'].pop(0)
#                     m[i]['paths'].pop(0)
#                     if m[first_v]['count'] <= 0 or m[i]['count'] <= 0:
#                         break

import json
import time
from collections import defaultdict
from operator import itemgetter


def three_sums(n):
        target = 0
        if not n or len(n) == 1:
            return []
        sn = set(n)
        if len(sn) <= 3:
            if len(sn) == 3 and sum(sn) == 0:
                return [sorted(sn)]
            elif len(sn) == 1 and len(n) >= 3 and n[0] == 0:
                return [[0, 0, 0]]
        m = defaultdict(int)
        for i in n:
            m[i] += 1
        res = []
        p = {}
        outer_index = 0
        for first_v in n:
            index = outer_index + 1
            for i in n[index:]:
                t = target - i - first_v
                if t in m:
                    mt = m[t]
                    if t == i or t == first_v:
                        if (t == i == first_v and mt < 3) or (mt < 2):
                            index += 1
                            continue
                    f = sorted([first_v, i, t])
                    # sorted花了40多ms
                    key = '%s_%s_%s' % (f[0], f[1], f[2])
                    if key in p:
                        index += 1
                        continue
                    res.append(f)
                    p[key] = None
                index += 1
            outer_index += 1
        g = itemgetter(0, 1, 2)
        res = sorted(res, key=lambda x: g(x))
        return res


def main():
    with open('large_sum_list', 'r') as f:
        large_list = json.load(f)
    ns = [[-5, 8, -2, 8, 0, 5, -7, 0, -6, -10], [0, 2, 2, 3, 0, 1, 2, 3, -1, -4, 2],
          [], [1], [0, 0], [-1, 0, 1, 2, -1, -4],
          ]
    for n in ns:
        res = three_sums(n)
        if not res:
            print(res)
        else:
            for i in res:
                print(i)
        print('-------------')
    start = time.time()
    x = three_sums(large_list)
    print(time.time() - start)
    print(len(x))
    print('---------0--------')
    k = [0] * 3000
    start = time.time()
    x = three_sums(k)
    print(time.time() - start)
    print(len(x))


if __name__ == '__main__':
    main()
