/*5. 最长回文子串
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
 
*/
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
bool isPalindrome(char* s, int left, int right) {
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
char* longestPalindrome(char* s) {
    int n = strlen(s);
    if (n < 2) {
        return s;
    }
    int maxLength = 1;
    int start = 0;
    bool dp[n][n];
    memset(dp, false, sizeof(dp));
    for (int i = n-1; i >= 0; i--) {
        for (int j = i; j < n; j++) {
            if (s[i]==s[j]) {
                if(j-i<3||dp[i+1][j-1]){
                    dp[i][j]=true;
                    if ((j-i+1) > maxLength) {
                        maxLength = j - i + 1;
                        start = i;
                    }
                }else{
                    dp[i][j]=false;
                }
            }
        }
    }
    s[start + maxLength] = '\0'; // 截断字符串
    return &s[start];
}