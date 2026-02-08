"""115. 不同的子序列
困难

给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数。

测试用例保证结果在 32 位有符号整数范围内。

 

示例 1：

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit
示例 2：

输入：s = "babgbag", t = "bag"
输出：5
解释：
如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
babgbag
babgbag
babgbag
babgbag
babgbag
 

提示：

1 <= s.length, t.length <= 1000
s 和 t 由英文字母组成"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m , n = len(s), len(t)
        
        # dfs(i, j) 表示：在 s[i:] 中匹配 t[j:] 的子序列个数
        # i: s 当前遍历到的下标
        # j: t 当前遍历到的下标
        def dfs(i, j):
            if i == m:
                return 0
            if j == n:
                return 1
            
            if s[i] == t[j]:
                return dfs(i + 1, j + 1) + dfs(i + 1, j)
            elif s[i] != t[j]:
                return dfs(i + 1, j)
        
        return dfs(0 , 0)
            
                