'''
这个是easy的

in-place去掉有序列表中的重复数字
'''


def remove_duplicates_from_sorted_array(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    count = 0
    parent_ele = None
    tail = 0
    for i in nums:
        if i != parent_ele:
            count += 1
            parent_ele = i
            if tail:
                nums[tail] = i
                tail += 1
        else:
            tail = count
    return nums, count


def main():
    ts = [[1, 1, 2], [1, 2, 3, 3, 4, 5, 5, 6, 7]]
    for t in ts:
        print(remove_duplicates_from_sorted_array(t))


if __name__ == '__main__':
    main()
