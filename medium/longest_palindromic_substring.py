'''
https://leetcode-cn.com/problems/longest-palindromic-substring/
最长回文子串
经典马拉车算法


理解如何使用上之前计算的结果(毕竟DP), 下面l前缀表示left, r表示right


-------lm--------------i------------------rm---------------------------

以上假设以i为中心的回文串半径是m, 那么求j为中心的回文串半径

-------lm--------------i---------j--------rm---------------------------

首先, j相对i的回文位置, lj(left j)

-------lm-------lj-------i---------j--------rm---------------------------


如果以lj为中心的回文串是在m范围呢, 假设为k, 那么有

-------lm----lk---lj--rk-----i---------j--------rm---------------------------

按照回文数的特性, 以lk到lj的元素, 是在以i为中心的回文数内, 那么可得lk-lj这些元素, 对应位置有j-lk1


-------lm----lk---lj--rk-----i----------j---lk1-----rm---------------------------

同理, lj-rk的元素，对应i的回文位置有rk1-j


-------lm----lk---lj--rk-----i------rk1----j---lk1-----rm---------------------------

那么又按照lj是回文数, 所以lk-lj, lj-rk的元素是相等的, 那么所以以j为中心的回文数中, rk1-j, j-lk1的数字是相等的, 那么j的长度至少为k

那么由于lj的长度是k, 所以lk-1和rk+1不相等, 而lk-1和rk+1相对于i的回味位置是lk1+1, rk1-1, 两者也不相等, 所以嘛, 以j为中心的回文长度就是k


这里我们利用了i和lj的回文数特性!!!!!!!!!!!!!!!!!!!!!!!!


如果lk的回文长度大于m, 比如下面以lj为中心的回文数长度边界超过了lm, 那么由lj的性质可知, 至少

lj - lk的元素等于rk-lj的元素, 那么lm对应于lj的位置为lm1, 那么lm-lj和lj-lm1的元素是相等的, 而这些元素对于i的回文位置为

j-m和lm2-j, 那至于对于j, m之外的元素和rk1-lm2的元素是否相等, 只能比较了


----lk---lm---lj--lm1---rk----i---rk1--lm2---j----m-------------------------


最后, 如果j大于m, 那么没办法, 继续中心拓展一个个比较

-------lm--------------i------------------rm----j-----------------------


最后,  以i为中心的最大回文数半径为n, 那么用一个数组p来存储,  有p[i] = n, 其中n也是回文数的总长度

而回文数的起始位置为 中心位置减去最长半径, 再除以2

longest_len = longest_radius
longest_start = (longest_center - longest_radius) // 2


执行用时 :296 ms, 在所有 python3 提交中击败了85.12%的用户

'''


def check_center_palindromic(i, pre_s, current_radius = 0):
    step = current_radius + 1
    while True:
        left = i-step
        right = i + step
        if left < 0 or right >= len(pre_s):
            break
        if pre_s[left] != pre_s[right]:
            break
        current_radius += 1
        step += 1
    return current_radius


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        pre_s = "$#" + "#".join(list(s)) + "#"
        i = 3
        len_array = [0] * len(pre_s)
        len_array[2] = 1
        longest_center = 2
        longest_radius = 1
        while i < len(pre_s):
            if i == 639:
                print("!")
            v = pre_s[i]
            if i > longest_center + longest_radius:
                current_radius = check_center_palindromic(i, pre_s)
                if current_radius >= longest_radius:
                    longest_radius = current_radius
                    longest_center = i
                len_array[i] = current_radius
            else:
                mirror_i = 2 * longest_center - i
                if mirror_i - len_array[mirror_i] <= longest_center - longest_radius:
                    if i == 646:
                        print("!")
                    current_radius = (longest_center + longest_radius) - i
                    current_radius = check_center_palindromic(i, pre_s, current_radius)
                    if current_radius >= longest_radius:
                        longest_radius = current_radius
                        longest_center = i
                    len_array[i] = current_radius
                else:
                    len_array[i] = len_array[mirror_i]
            i += 1
        longest_len = longest_radius
        longest_start = (longest_center - longest_radius) // 2
        if longest_len == 0:
            return ""
        return s[longest_start:longest_start+longest_len]





def main():
    ss = ["tfekavrnnptlawqponffseumswvdtjhrndkkjppgiajjhklqpskuubeyofqwubiiduoylurzlorvnfcibxcjjzvlzfvsvwknjkzwthxxrowidmyudbtquktmyunoltklkdvzplxnpkoiikfijgulbxfxhaxnldvwmzpgaiumnvpdirlrutsqenwtihptnhghobrmmzcsrhqgdgzrvvitzgsolsxjxfeencvpnltxeetmtzlwnhlvgtbhkicivylfjhhfqteyxewmnewhmsnfdyneqoywgsgptwdlzbraksgajciebdchindegdfmayvfkwwkkfyxqjcv",
          "aaaa", "abc", "cbbd", "babad", "abcb", "", "a", "ab"]
    t = "$#" + "#".join(list(ss[0])) + "#"
    print(t.index("#f#k#w#w#k#k#f#"))
    so = Solution()
    for s in ss:
        print(s, so.longestPalindrome(s))
    return
    
    
if __name__ == "__main__":
    main()
    
