"""5. 最长回文子串
中等
提示
给你一个字符串 s，找到 s 中最长的 回文 子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成
 
"""

class Solution:
    def isPalindrome(self, s:str, left:int, right:int) -> bool:
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # if n == 0:
        #     return ""
        if n < 2:
            return s
        dp = [[False]*n for _ in range(n)]
        # 这里太聪明了，通过二维数组的两个下标来代表字符串的起始和结束位置，从而表示子串
        max_len =1
        start = 0

        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i]==s[j]:
                    if j-i<=2 or dp[i+1][j-1]:
                        dp[i][j]=True
                        current_len = j - i + 1
                        if current_len>max_len:
                            max_len = j-i+1
                            start = i
                    else:
                        dp[i][j]=False
        # for i in range(n):
        #     for j in range(i,n):
        #         if(self.isPalindrome(s,i,j)):
        #             # dp[i][j]=True
        #             current_len = j - i + 1
        #             if current_len>max_len:
        #                 max_len = j-i+1
        #                 start = i
        # # s[start+max_len]='\0'
        return s[start:start+max_len]