"""11. 盛最多水的容器
中等
相关标签
premium lock icon
相关企业
提示
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

 

示例 1：



输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_area = 0
        # n = len(height)
        # for i in range(n):
        #     current_area = 0
        #     for j in range(i+1,n):
        #         current_area = min(height[i], height[j]) * (j - i)
        #         max_area = max(max_area,current_area)
        # return max_area
        n = len(height)
        left, right = 0, n - 1
        max_area = 0
        max_height = max(height)
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            current_area = width * h
            max_area = max(current_area,max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1            
            if max_area > (max_height * (right-left)):
                break
        return max_area