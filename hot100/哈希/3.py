"""128. 最长连续序列
中等
相关标签
premium lock icon
相关企业
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
示例 3：

输入：nums = [1,0,1,2]
输出：3
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash_map = {}       
        # hash_map2 = {}
        # for num in nums:
        #     hash_map[num] = True
        # max_count = 0
        # for x in hash_map:

        #     if x in hash_map2:
        #         continue
        #     current_num = x

        #     current_count = 1
        #     hash_map2[current_num] = True
        #     while (current_num + 1) in hash_map:
        #         current_num += 1
        #         current_count += 1
        #         hash_map2[current_num] = True
        #     if current_count > max_count:
        #         max_count = current_count
        # return max_count
        num_set = set(nums)
        max_count = 0
        for x in num_set:
            if x - 1 not in num_set:
                current_num = x
                current_count = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_count += 1
                max_count = max(max_count,current_count)
        return max_count

