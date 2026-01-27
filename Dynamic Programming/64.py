"""64. 最小路径和
中等

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

 

示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        # for i in range(1,m):
        #     dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+grid[i][0]
            for j in range(1,n):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]
    
    def faster_minPathSum(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])

        dp = [0]*n
        dp[0] = grid[0][0]
        for i in range(1,n):
            dp[i] = dp[i-1]+grid[0][i]
        # 这一步对于第一行，让dp这个一维数组记录第一行从左到右的累加和
        for i in range(1,m):
            for j in range(0,n):
                if j == 0:
                    dp[j] = dp[j] + grid[i][0]
                    # dp[0]记录了第一列从上到下的累加和
                    # 每次i变动，换行的时候 dp[0]都在记录当前grid[i][0]的值？
                else:
                    dp[j] = min(dp[j-1],dp[j])+grid[i][j]
                    # 对于当前行来说，这一行执行时dp[j]还没有变动，记录的是上一次i即grid[i-1][j]的值
                    # 所以dp[j-1]是上一次j变化，即同样的行，左边那一列所对应的grid[i][j-1]的值
                    # 这样就完成了对于当前grid[i][j]的最小路径和的计算
        return dp[n-1]