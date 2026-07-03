"""
代码
测试用例
测试用例
测试结果
49. 字母异位词分组
中等
相关标签
premium lock icon
相关企业
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

 

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

解释：

在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
示例 2:

输入: strs = [""]

输出: [[""]]

示例 3:

输入: strs = ["a"]

输出: [["a"]]

 

提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n = len(strs)
        # alphabet_count = [[0]*26 for _ in range(n)]
        # for idx, s in enumerate(strs):
        #     for char in s:
        #         position = ord(char)-ord("a")
        #         alphabet_count[idx][position]+=1
        # used = [False] * n
        # ret = []
        # for i in range(n):
        #     if used[i]:
        #         continue # 跳出这次i循环
        #     group = [strs[i]]
        #     for j in range(i+1,len(strs)):
        #         is_same = True
        #         for letter in range(26):
        #             if alphabet_count[i][letter] != alphabet_count[j][letter]:
        #                 is_same = False
        #                 break
        #         if is_same:
        #             group.append(strs[j])
        #             used[j] = True
        #     ret.append(group)
        # return ret
        n = len(strs)
        hash_map = {}
        for idx, string in enumerate(strs):
            letter_count = [0]*26
            for char in string:
                letter_count[ord(char) - ord("a")] += 1
            string_tuple = tuple(letter_count)
            if string_tuple in hash_map:
                hash_map[string_tuple].append(string)
            else:
                hash_map[string_tuple] = [string]

        return list(hash_map.values())


            