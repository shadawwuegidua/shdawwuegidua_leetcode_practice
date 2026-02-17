"""300. 最长递增子序列
中等

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
 

提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

进阶：

你能将算法的时间复杂度降低到 O(n log(n)) 吗?"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp  = [1] * n
        # dp[i] 表示以 nums[i] 结尾的最长递增子序列的长度
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    def lengthOfLIS_optimized(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            if tails == [] or num > tails[-1]:
                tails.append(num)
            else:
                left, right = 0, len(tails) - 1
                while left < right:
                    current_location = (left + right) //2
                    if tails[current_location] < num:
                        left = current_location + 1
                    else:
                        right = current_location
                # tails[current_location] = num
                # 这里不是 current_location，而是 left 或 right，
                # 因为 current_location 是在 while 循环中计算的，循环结束的时候它的值保留了上一个值
                # 而循环结束后 left 和 right 会相等，指向正确的位置。
                tails[left] = num
                 
        return len(tails)