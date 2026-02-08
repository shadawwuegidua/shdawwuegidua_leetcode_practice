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
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # dfs(i, j) 表示：在 s[i:] 中匹配 t[j:] 的子序列个数
        # i: s 当前遍历到的下标
        # j: t 当前遍历到的下标
        # def dfs(i, j):
        for i in range(m + 1):
            dp[i][n] = 1
        for i in range(m - 1, -1, -1):
            # 这里是从m-1开始一直到0
            for j in range(n - 1, -1, -1):
                # if i == m:
                #     return 0
                # 这里应该放在后面，因为是从0,0开始调用的，如果放在前面的话，第一次调用就会返回0了
                # if j == n:
                    # dp[i][j] = 1
                    # return 1
                if i == m:
                    dp[i][j] = 0
                    # return 0   

                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                    # return dp[i][j]
                    # return dfs(i + 1, j + 1) + dfs(i + 1, j)
                # elif s[i] != t[j]:
                else:
                    dp[i][j] = dp[i + 1][j]
                # return dfs(i + 1, j)
        
        # return dfs(0 , 0)
        dp[m][n] = 1
        import collections
        def bfs(i: int , j: int) -> int:
            queue = collections.deque([(i, j)])
            # collections类的deque
            count = 0
            while queue:
                i, j = queue.popleft()
                # deque的popleft方法，弹出最左边的元素

                if j == n:
                    count += 1
                    continue
                if i == m:
                    continue

                if s[i] == t[j]:
                    queue.append((i + 1, j + 1))
                #     queue.append((i + 1, j))
                # else:
                #     queue.append((i + 1, j))
                queue.append((i + 1, j))
            return count
        return bfs(0, 0)
        # return dp[0][0]
            
                