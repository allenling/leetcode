

def two_sum(n, target):
    if not n or len(n) == 1:
        return []
    len_n = len(n)
    m = {}
    res = []
    index = 0
    while index < len_n:
        i = n[index]
        if i not in m:
            m[i] = {'count': 1, 'paths': [index]}
        else:
            m[i]['count'] += 1
            m[i]['paths'].append(index)
        index += 1
    index = 0
    while index < len_n:
        i = n[index]
        if m[i]['count'] <= 0:
            index += 1
            continue
        t = target - i
        if t in m:
            if m[t]['count'] <= 0:
                index += 1
                continue
            if t == i:
                if len(m[t]['paths']) == 1:
                    index += 1
                    continue
                path = m[t]['paths'].pop(m[t]['paths'].index(index) + 1)
            else:
                path = m[t]['paths'].pop(0)
            res.append(sorted([index, path]))
            if m[i]['count'] > 0:
                m[i]['count'] -= 1
                m[i]['paths'].remove(index)
            if m[t]['count'] > 0:
                m[t]['count'] -= 1
        index += 1
    return res


def main():
    target = 9
    print('---------9--------------')
    ts = [[4.5, 4.5], [4.5, 7, 2], [2, 7, 11, 15], [3, 6, 3],
          [2, 6, 7, 2, 3, 8], [], [2],
          ]
    for t in ts:
        print(t, two_sum(t, target))
    print('---------6--------------')
    ta1 = 6
    tts = [[3, 2, 4]]
    for t in tts:
        print(t, two_sum(t, ta1))
    return


if __name__ == '__main__':
    main()
