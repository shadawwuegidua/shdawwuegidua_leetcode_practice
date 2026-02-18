"""646. 最长数对链
中等

给你一个由 n 个数对组成的数对数组 pairs ，其中 pairs[i] = [lefti, righti] 且 lefti < righti 。

现在，我们定义一种 跟随 关系，当且仅当 b < c 时，数对 p2 = [c, d] 才可以跟在 p1 = [a, b] 后面。我们用这种形式来构造 数对链 。

找出并返回能够形成的 最长数对链的长度 。

你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

 

示例 1：

输入：pairs = [[1,2], [2,3], [3,4]]
输出：2
解释：最长的数对链是 [1,2] -> [3,4] 。
示例 2：

输入：pairs = [[1,2],[7,8],[4,5]]
输出：3
解释：最长的数对链是 [1,2] -> [4,5] -> [7,8] 。
 

提示：

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000"""
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # dp 方案
        pairs.sort(key = lambda x: x[0])
        n = len(pairs)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        # 贪心方案
        pairs.sort(key = lambda x: x[1])
        # tails = []
        # for pair in pairs:
        #     if tails == [] or pair[0] > tails[-1][1]:
        #         tails.append(pair)
        # return len(tails)
        current_end = float('-inf')
        count = 0
        for pair in pairs:
            if pair[0] > current_end:
                count += 1
                current_end = pair[1]   
                # pair尾部已经排序好了，所以我们只需要更新 current_end 就可以了
        # return count

        tails = []
        for pair in pairs:
            if tails == [] or pair[0] > tails[-1][1]:
                tails.append(pair)
        return len(tails)