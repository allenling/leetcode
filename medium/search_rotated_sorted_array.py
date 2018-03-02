'''
没看答案
一个单调递增的数组, 被旋转了, 旋转轴不懂，求给定一个值在该数组的下标.
0 1 2 4 5 6 7 旋转为 4 5 6 7 0 1 2
其实关键点就是找到旋转轴, 查找嘛，还是有序的，就想到了用二分.

然后根据给定值是在前半个数组还是后半个数组，再用二分查找, 比如上面的，找到0, 然后给定的值是0-2之前，就二分后半部分数组，给出的值是4-7之间，则二分前半个数组

首先, 旋转轴, 不，应该说是分隔数组的值, 称为n, n的特点是它的前一个, 后一个不是单调的, 比如上面的4 5 6 7 0 1 2,
n=0, 其前一个7和后一个1不是递增的, 所以怎么找这个值呢?
显然我们就算用二分找到中间值, 设为x, 其下标为ix, 之后，如果只是简单的判断ix-1和ix+1是否是递增的也不好，因为有可能是递增的呀:

设数组a为
60,70,0,10,18,20,35,44, 中间下标ix为4, x值为18, 其前一个，后一个还是递增的，我们也不可能两边遍历的呀~~~所以关键点就是
我们找到中间值之后，如何确定下一个查找的方向，是往左还是往右????在二分中，确定方向是说查找值v大于或者小于中间值x, 这样就确定了方向了,
我们这里怎么办? 例子中我们知道我们得到18之后，应该往左边找，为什么呢？因为左边存在大于18的数字，所以，我们只需要判断左边是否
存在比18大，或者右边是否存在比18小的值，我们就知道下一个二分的方向了. 所以，我们直接判断a[start]是否大于a[mid]或者a[end]是否小于a[mid]
就知道方向了!!!!!

还有很多边界条件，比如没有翻转，空列表输入等等, 就很烦
快于75%左右
'''


def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = -1
    while first <= last:
        if last - first == 1 or last == first:
            if alist[last] == item:
                found = last
            elif alist[first] == item:
                found = first
            break
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = midpoint
            break
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def find_rotated(n):
    start, end = 0, len(n) - 1
    if n[end] > n[start]:
        # 都是有序的，那么就是没有翻转咯，直接返回中间值
        return start + int((end - start) / 2)
    while True:
        if end - start == 1 and n[start] > n[end]:
            mid = end
            break
        mid = start + int((end - start) / 2)
        if n[start] > n[mid]:
            end = mid
        elif n[end] < n[mid]:
            start = mid
    return mid


def check_return(n, v):
    if not n:
        return -1
    elif len(n) == 1:
        if n[0] != v:
            return -1
        else:
            return 0
    elif v == n[0]:
        return 0
    elif v == n[-1]:
        return len(n) - 1
    return None


def search_rotated_sorted_array(n, v):
    c = check_return(n, v)
    if c is not None:
        return c
    rotated_index = find_rotated(n)
    index_prefix = 0
    if n[0] < v <= n[rotated_index - 1]:
        index = binary_search(n[:rotated_index], v)
    elif n[rotated_index] < v < n[-1]:
        index_prefix = rotated_index
        index = binary_search(n[rotated_index:], v)
    elif v == n[rotated_index]:
        index = rotated_index
    else:
        index = -1
    if index == -1:
        return index
    return index_prefix + index


def main():
    a = [4, 5, 6, 7, 0, 1, 2]
    for i in a:
        index = search_rotated_sorted_array(a, i)
        print(i, index)
    print(search_rotated_sorted_array([], 5))
    a = [1, 3, 5]
    for i in a:
        index = search_rotated_sorted_array(a, i)
        print(i, index, a.index(i) == index)
    print(search_rotated_sorted_array(a, 7))
    a = [5, 3, 1]
    for i in a:
        index = search_rotated_sorted_array(a, i)
        print(i, index, a.index(i) == index)
    print(search_rotated_sorted_array(a, 7))
    return


if __name__ == '__main__':
    main()
