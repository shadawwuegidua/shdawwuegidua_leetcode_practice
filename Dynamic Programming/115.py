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
        
        def bfs_optimized():
            memo = {0: 1}
            # 这里实际上字典的结构是 {j: count}，表示在s的当前遍历位置下，t的j位置匹配成功的子序列个数
            # python中字典的key是唯一的，所以当j相同时，count会累加
            for char_s in s:
                next_memo = memo.copy()
                for j, count in memo.items():
                # items()方法返回一个可迭代的视图对象，包含字典的键值对
                    if j < n and char_s == t[j]:
                        next_memo[j + 1] = next_memo.get(j + 1, 0) + count
                # get()的意思是比如memo.get(j + 1, 0)，如果j + 1在next_memo中存在，就返回next_memo[j + 1]的值，否则返回0
                    next_memo[j] = next_memo.get(j, 0) + count
                memo = next_memo
            return memo.get(n, 0)

        def dp_optimized_dict():
            # key: 匹配到了 t 的第几个字符 (也就是 j)
            # value: 有多少种方案 (count)
            # 初始化: 匹配了 0 个字符的方案数为 1
            memo = {0: 1} 

            # 遍历 s 的每一个字符 (相当于 i 的循环)
            for char_s in s:
                # 必须在这个循环内倒序处理，或者像你代码里那样新建一个 next_memo
                # 为了方便理解，我们用新建字典的方式 (对应你的 next_memo)
                
                # 也就是：我们要根据上一轮的 memo，算出这一轮的 memo
                # new_memo 继承 memo 的所有老本 (相当于 dp[i][j] = dp[i-1][j])
                # 因为你不选 char_s 的话，原来的匹配方案依然成立
                new_memo = memo.copy() 
                
                for j, count in memo.items():
                    # j < n: 还没匹配完 t
                    # char_s == t[j]: 当前 s 的字符正好是 t[j] 需要的字符
                    if j < n and char_s == t[j]:
                        # 我们可以扩展匹配长度！从 j 变成 j+1
                        # get(j+1, 0) 是为了防止 j+1 这个键还没出现过
                        new_memo[j + 1] = new_memo.get(j + 1, 0) + count
                
                # 更新状态
                memo = new_memo
            
            # 最后返回匹配了 n 个字符 (即整个 t) 的方案数
            return memo.get(n, 0)
        return dp_optimized_dict()  
        # return bfs_optimized()

        # return dp[0][0]

