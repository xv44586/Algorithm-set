"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true



dp[i][j] 表示s[0, i-1] 和 p[0, j-1]是否匹配
初始解:
    dp[0][0] = true; // 两个空字符串
    dp[0][1] 和 dp[1][0] 均是false
状态转义方程：
    如果p[j - 1]不是*也不是.则判断 s[i - 1] == p[j - 1] && dp[i - 1][j - 1]
    如果p[j - 1]是. 则dp[i][j] = dp[i - 1][j - 1]
    如果p[j - 1]是* 则分三种情况
        1. 匹配0个  dp[i][j] = dp[i][j - 2]
        2. 匹配1个  dp[i][j] = dp[i][j - 1]
        3. 匹配多个 dp[i][j] = dp[i - 1][j] && s[i - 1] == p[j - 2] || p[j - 2] == '.'
"""