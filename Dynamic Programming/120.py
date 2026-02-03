"""120. 三角形最小路径和
中等
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

 

示例 1：

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
示例 2：

输入：triangle = [[-10]]
输出：-10
 

提示：

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

进阶：

你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？"""
class Solution:
   def minimumTotal(self, triangle: List[List[int]]) -> int:
      n = len(triangle)
      dp = [[0] * n for _ in range(n)]
      dp[0][0] = triangle[0][0]
      for i in range(1,n):
         dp[i][0] = dp[i-1][0]+triangle[i][0]
         dp[i][i] = dp[i-1][i-1]+triangle[i][i]
         for j in range(1,i):
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
      return min(dp[n-1])
      # 我发现这里min函数能直接传列表，询问gemini得知这是python的内置函数特性，可以直接对可迭代对象进行操作
      # 这又出现了新的问题，什么是可迭代对象？迭代是什么意思？
      # 可迭代对象是指可以逐个访问其元素的对象，比如列表、元组、字符串、字典等。内置的min函数可以接受一个可迭代对象作为参数，并返回其中的最小值。
      # 迭代是指逐个访问可迭代对象中的元素的过程。通过迭代，可以对每个元素进行操作，比如比较大小、计算总和等。