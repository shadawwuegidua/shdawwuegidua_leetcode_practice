"""740. 删除并获得点数
中等

提示
给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

 

示例 1：

输入：nums = [3,4,2]
输出：6
解释：
你可以执行下列步骤：
- 删除 4 获得 4 个点数，因此 3 也被删除。nums = [2]。
- 之后，删除 2 获得 2 个点数。nums = []。
总共获得 6 个点数。
示例 2：

输入：nums = [2,2,3,3,3,4]
输出：9
解释：
你可以执行下列步骤：
- 删除 3 获得 3 个点数。所有的 2 和 4 也被删除。nums = [3,3]。
- 之后，再次删除 3 获得 3 个点数。nums = [3]。
- 再次删除 3 获得 3 个点数。nums = []。
总共获得 9 个点数。
 

提示：

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104"""

"""本题如果不考虑使用动态规划的话，应该考虑对数组的每一个元素尝试删除后再执行的结果，通过另一个数组记录。
但是很容易看出来对于元素的第二次选择会出现分支的选项，这样会导致需要额外的东西来帮助记录最后得到的点数。
再删除第i个元素后，最终得到的点数是nums[i]，这时候所有等于nums[i]+-1的元素也会被删除。这就是一次操作。
这次操作结束会后数组剩下的元素都会是>nums[i]+1以及<nums[i]]-1，以及==nums[i]的元素。要从这里删除。"""

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # ret = [0] * len(nums)
        # nums.sort()
        # n = len(nums)
        # ret[0]=nums[0]
        # for i in range(0,n):
        #     ret

        # 第一步：统计每个数字能带来的总点数
        # 用一个数组，索引是数字本身，值是该数字的总点数
        max_num = max(nums)
        total_points = [0] * (max_num + 1)
        
        for num in nums:
            total_points[num] += num


        # dp = [0] * (max_num + 1)

        # for i in range(1, max_num + 1):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + total_points[i])        

        # return dp[max_num]

        memo = {}
        # 第二步：定义递归函数solve
        # solve(i) 表示：从数字i开始考虑到max_num，能获得的最大点数
        def solve(i):
            if i in memo:
                return memo[i]
            # 递归终止条件：如果超出范围，返回0
            if i > max_num:
                return 0
            
            # 选择1：拿数字i的点数
            # 如果拿了i，就不能拿i+1，所以下一步跳到i+2
            take_i = total_points[i] + solve(i + 2)
            
            # 选择2：不拿数字i的点数
            # 如果不拿i，那么i+1可以自由选择，所以下一步去i+1
            skip_i = solve(i + 1)
            
            # 返回两种选择中的最大值
            result = max(take_i, skip_i)
            memo[i]= result
            return result
        
        # 从数字0开始递归（虽然题目说nums[i]>=1，但为了代码统一从0开始也可以）
        return solve(0)
