'''
56ms, 超过56.46%
'''


def new_two_sum(data, target):
    if not data:
        return []
    res = []
    data_info = {}
    for index, value in enumerate(data):
        if value not in data_info:
            data_info[value] = {'count': 1, 'indexes': set([index])}
        else:
            data_info[value]['count'] += 1
            data_info[value]['indexes'].add(index)
    for index, value in enumerate(data):
        current_info = data_info[value]
        if current_info['count'] == 0:
            current_info = None
            continue
        left = target - value
        left_info = data_info.get(left, None)
        if left_info is None:
            continue
        if left_info['count'] == 0:
            left_info = None
            continue
        current_info['indexes'].remove(index)
        current_info['count'] -= 1
        if left_info['count'] == 0:
            left_info = None
            continue
        left_info['count'] -= 1
        next_index = left_info['indexes'].pop()
        res.append([index, next_index])
    return res[0] if res else []


def main():
    print('---------6--------------')
    ta1 = 6
    tts = [[3, 2, 4]]
    for t in tts:
        print(t, new_two_sum(t, ta1))
        print('~~~~~~~~~~~~~~~')
    target = 9
    print('---------9--------------')
    ts = [[2, 7, 11, 15],
          [4.5, 4.5], [4.5, 7, 2], [2, 7, 11, 15], [3, 6, 3],
          [2, 6, 7, 2, 3, 8], [], [2],
          ]
    for t in ts:
        print(t, new_two_sum(t, target))
        print('~~~~~~~~~~~~~~~')
    return


if __name__ == '__main__':
    main()
