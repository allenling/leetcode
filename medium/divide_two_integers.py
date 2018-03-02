'''
关于取反码补码
http://www.cnblogs.com/piperck/p/5829867.html
我不会，不知道，我看答案的，阿西吧
'''
import sys


def divide_two_integers(dividend, divisor):
        max_int = 2147483647
        min_in = -2147483648
        m, n = dividend, divisor
        if n == 0:
            return -1
        if m <= min_in and n == -1:
            return max_int
        if m == 0:
            return 0
        sym = False
        if n == -1 and dividend == -2147483648:
            return 2147483647
        if (m < 0 and n > 0) or (n < 0 and m > 0):
            sym = True
        m, n = abs(m), abs(n)
        if n > m:
            return 0
        ele = []
        res = 1
        while res > 0:
            res = len(bin(m)) - len(bin(n))
            if res > 0:
                mn = n << res
                if m == mn:
                    ele.append(1 << res)
                    break
                elif m < mn:
                    ele.append(1 << (res - 1))
                    m = m - (n << (res - 1))
                elif m > mn:
                    ele.append(1 << res)
                    m -= mn
            else:
                if m >= n:
                    ele.append(1)
        divi = sum(ele)
        if sym:
            divi = -divi
        return divi


def other(dividend, divisor):
    digits = 0
    first_d = divisor
    while dividend > first_d:
        first_d <<= 1
        digits += 1
    if first_d == dividend:
        return 2 ** digits
    res = 0
    digits -= 1
    while digits >= 0:
        if dividend >= (divisor << digits):
            dividend -= (divisor << digits)
            res += (1 << digits)
        digits -= 1
    return res


def main():
    ts = [[-2147483648, -3],
          [2147483648, -1], [-1124481825, -17740490], [5, 2],
          [100, 1], [3, 5], [5, 3], [100, 3], [0, 1], [1, 0],
          [10, 8], [100, 63], [-100, 3], [-3, 100], [-100, -30],
          ]
    for t in ts:
        print(t, divide_two_integers(*t))
    print('--------------------------------')
    print(other(87, 4))
    return


if __name__ == '__main__':
    main()
