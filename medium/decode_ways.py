'''
https://leetcode.com/problems/decode-ways/description/
用动态规划, 自己没解出来

参考
1. https://blog.csdn.net/u011095253/article/details/9248109
2. https://segmentfault.com/a/1190000003813921
参考1, 2中都解释到, dp数组的计算规则如下面, 但是不明白为什么:

1. 如果dp[i]所对应的的单个字符可以解码，那么dp[i]就包括前dp[i-1]位所积累的组合数 dp[i] = dp[i-1]

2. 如果不仅dp[i]所对应的的单个字符可以解码，dp[i-1] － dp[i]，两个字符组成的也可以解码，那么不仅包括dp[i-1]积累的组合数，也包括dp[i-2]位积累的组合数 dp[i] = dp[i-1] + dp[i-2]
'''


def decode_ways(n):
    len_n = len(n)
    if n == '0' or len_n == 0:
        return 0
    if len_n == 1:
        return 1
    if n[0] == '0':
        return 0
    dp = {0: 1, 1: 1}
    for index in range(2, len_n + 1):
        dp[index] = 0
        if 10 <= int(n[index - 2: index]) <= 26:
            dp[index] += dp[index - 2]
        if int(n[index - 1: index]) != 0:
            dp[index] += dp[index - 1]
    return dp[len_n]


def main():
    ds = ['00', '10', '', '0', '12', '121', '12192', '9124', '121212', '12121']
    for d in ds:
        print(decode_ways(d))
    return


if __name__ == '__main__':
    main()
