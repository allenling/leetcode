'''
思路是回溯

一开始没解出来, 然后参考了其他人的思路, 他们的代码当然看不懂了

然后参考了回溯的思路, 回溯是求出解空间(所有可能解), 然后遍历, 一般是dfs遍历

然后我这里主要是用数组保存所有的解的可能性, 过leetcode时间是100ms, 然后快于66.05%

最快的是60ms, 也就是使用dfs

例子: [2, 3, 5], 8

sum_list = [[], 0]], 第一个元素是元素列表, 第二个元素是和

1. 一开始遍历到2, 然后我们有

   sum_list = [[], 0], [[2], 2], [[2, 2], 4], [[2, ,2, 2], 6]]

   也就是可能的和是0, 2, 2+2, 2+2+2

2. 然后遍历到3, 0和3的可能和是0 + 3 = 3, 0 + 3 + 3 = 6, 0 + 3+ 3+ 3 = 9 > 7,所以9不能加入到sum_list

   此时, sumlist = [[], 0], [[2], 2], [[2, 2], 4], [[2, ,2, 2], 6],
                   [[3], 3], [[3, 3], 6],
                  ]

    接着是2和3的可能和的值: 2 + 3 = 5, 2 + 3 + 3 = 8 >7, 所以8不能加入到可能和的列表,

   sum_list = [[], 0], [[2], 2], [[2, 2], 4], [[2, ,2, 2], 6],
               [[3], 3], [[3, 3], 6], [[2, 3], 5],
               ]

   然后接下来是求2 + 2和3的和, 可能的值有

   2 + 2 + 3 = 7 == 7, 这里7 == 7, 所以我们没必要再计算2 + 2+ 3+ 3了, 所以记住2, 2, 3, 此时sum_list不变

   然后继续求2 + 2 + 2和3的和的可能值

   2 + 2 + 2 + 3 = 9 > 7, 所以结束循环

   此时我们把0, 2, 3所有的和的可能值都计算出来了

3. 依次计算出所有的可能和

4. 其他的答案是使用递归dfs, 这里不用, 好理解

'''


def combination_sum(nlist, target):
    if not nlist:
        return []
    res = []
    sum_list = [[[], 0]]
    new_nlist = sorted(nlist)
    for number in new_nlist:
        len_sum_list = len(sum_list)
        for i in range(len_sum_list):
            key, value = sum_list[i]
            while True:
                value += number
                key = key + [number]
                if value < target:
                    sum_list.append([key, value])
                elif value == target:
                    res.append(key)
                    break
                else:
                    break
    return res


def main():
    datas = [[[2, 3, 5], 8],
             [[2, 3, 6, 7], 7],
             ]
    for data, target in datas:
        print(combination_sum(data, target))
    return


if __name__ == '__main__':
    main()
