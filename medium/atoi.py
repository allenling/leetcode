'''
快于50%左右
'''


def atoi(input_str):
    max_v = 2147483647
    min_v = -2147483648
    num = 0
    input_str = input_str.strip()
    if not input_str:
        return num
    new_list = list(input_str)
    res = []
    sym = new_list[0]
    if sym not in ['+', '-']:
        if not ('0' <= sym <= '9'):
            return num
        else:
            res.append(sym)
    for n in new_list[1:]:
        if '0' <= n <= '9':
            res.append(n)
        else:
            break
    if res:
        if sym and sym in ['+', '-']:
            res.insert(0, sym)
        res = ''.join(res)
        num = int(res)
        if num > max_v:
            num = max_v
        elif num < min_v:
            num = min_v
    return num


def main():
    te = ['1', '+', '123sdgd123fh', '2147483647', '-2147483648', '-2147483649', '2147483648',
          '-2+1-3', '', '+2', '-2', '+-2', 'sfsa-2r']
    for t in te:
        print(t, atoi(t))
    return


if __name__ == '__main__':
    main()
