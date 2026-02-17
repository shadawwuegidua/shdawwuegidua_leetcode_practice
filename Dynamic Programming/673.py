"""673. 最长递增子序列的个数
中等

给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。

注意 这个数列必须是 严格 递增的。

 

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
 

提示: 

1 <= nums.length <= 2000
-106 <= nums[i] <= 106"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # tails = []
        # for num in nums:
        #     if tails == [] or num > tails[-1]:
        #         tails.append(num)
        #     else:
        #         left, right = 0, len(tails) - 1
        #         while left < right:
        #             current_location = left + right // 2
        #             if tails[current_location] < num:
        #                 left = current_location + 1
        #             else:
        #                 right = current_location
        #         tails[left] = num
        #         # 这里进行的实际上是替换，它破坏了历史的信息，所以我们不能使用这种方法来计算最长递增子序列的个数
        #         # tails[i]表示长度为i + 1的最长递增子序列中，可能的结尾元素的最小值
        #         # 实际上是一种贪心算法，因为我们希望在长度相同的情况下，结尾元素越小越好
        #         # 这样得到的最长递增子序列的长度是正确的，最有“潜力”的
                
        # length_of_lis = len(tails)
        
        n = len(nums)
        dp  = [1] * n
        count = [1] * n
        # dp[i] 表示以 nums[i] 结尾的最长递增子序列的长度
        for i in range(n):
            for j in range(i):
                # 因为这个子序列的顺序必须和原数组的顺序一致，所以我们只能在 i 之前的元素中寻找比 nums[i] 小的元素
                if nums[i] > nums[j]:
                    # dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                        # 当我们找到一个更长的递增子序列时，前面count统计作废，集成count[j]的值
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]
        # return max(dp)
        longest = max(dp)
        result = 0
        for i in range(n):
            if dp[i] == longest:
                result += count[i]
        return result