'''
longest_substring_without_repeating_characters
无重复字符的最长子串


主要是动态规划的思路, 肯定能O(n)的

思路, 其中x为元素, x1表示第一个x, x2表示第二个x

left
    ---x1---------x2-------x3---------

left=0, 遇到了第二个x(x2), 它是重复的, 那么显然我们的最长子串就是left-(x2-1), 此时吧Left设置为x2+1

                    left
    ---x1---------x2-------x3---------

然后继续, 如果我们遇到x3, 那么其实x3和x1重复我们不需要管, 因为x2和x1已经重复了, 也就是说left的位置说明的是

                    left
    ---x1---o2------x2-------o2---------

left之前已经有重复元素了, 此时如果一个元o2素的重复元o1是在left之前, 那完全没有意义, 因为任何left之前的元素

和left之后的元素, 是不能形成子串的, 因为left之前就有两个相同的元素打断了子串, 所以

如果o1的位置是left之前, 没关系, 继续走, 此时我们的子串继续增长, 主要要记录元素o的最后位置是o2

也就是说从left开始没遇到重复元素的子串, 此时我们遇到重复子串实在left之后, 说明当前子串被截断了, 要

计算长度了

所以最最重要的就是left位置的含义!!!!!!!!!!!!!!!!!

执行用时 :
48 ms, 在所有 python3 提交中击败了99.91%的用户

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        longest = 0
        last = dict()
        
        for index, value in enumerate(s):
            if value in last:
                # 判断是否在left之后, 不在的话, 当前子串不需要被打断
                if last[value] < left:
                    pass
                else:
                    # 如果是在left之后, 那么说明当前子串要被打断了, 计算子串的长度和longest比较吧
                    # 注意的是, 子串被打断了, 那么子串的最长长度就是index - left!
                    # 不要考虑重复元素
                    sub_len = index - left
                    if sub_len > longest:
                        longest = sub_len
                        # 重置left
                    left = last[value] + 1
            last[value] = index
        # 考虑下一直走到最后都没有重复元素的话
        if len(s) - left > longest:
            longest = len(s) - left

        return longest



def main():
    ss = ["abcabcbb", "bbbb", "bcbbbb", "abcdefagp", "", "a"]
    for s in ss:
        x = Solution()
        res = x.lengthOfLongestSubstring(s)
        print(s, res)
    return


if __name__ == "__main__":
    main()
