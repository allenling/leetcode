'''
note:做法自然是base于2-sum，遍历数组的每一个数为target，寻找其他数的和为该数的负数 -target

关键在于时间复杂度的优化，复杂度O(n^2)
优化点1: 优先对数组排序，这样碰到某一个target，只用对其后的数组求该-target的2sum，同时能保证最后返回的三元组一定有序
优化点2：结果用set()来存，这样添加结果时候要用.add()方法，将结果三元组保存为tuple (target, -target-i, i) ，
而不能是list [target, -target -i, i] (python里list是unhashable，不能加到set中，最终结果map成list
优化点3: 最外层遍历数组的时候，已经算过的target存入字典中，下次碰到不再计算，否则会卡case 322/323，一个全是[0,0,0,0...]的case

如果miss掉优化点1和2会卡3个case，miss掉优化3会卡最后2个case

作者：sylvainwang
链接：https://www.jianshu.com/p/9b18a96f558b
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
'''


def three_sums(nums):
    if not nums or len(nums) < 3:
        return []
    nums.sort()
    res = set()
    d_key = {}

    for i in range(len(nums)):
        target = nums[i]
        d = {}
        if target in d_key:
            continue
        for j in nums[i + 1:]:
            if -target - j in d:
                res.add((target, -target - j, j))
            else:
                d[j] = 1
        d_key[target] = 1

    return [list(i) for i in res]


def main():
    ns = [[-5, 8, -2, 8, 0, 5, -7, 0, -6, -10], [0, 2, 2, 3, 0, 1, 2, 3, -1, -4, 2],
          [], [1], [0, 0], [-1, 0, 1, 2, -1, -4],
          ]
    for n in ns:
        res = three_sums(n)
        print(res)
    return


if __name__ == '__main__':
    main()
