# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba"也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = ''
        for x in range(len(s)):
            for i in range(len(s) - x):
                r = s[i:i + x + 1]
                if isPalindrome(r):
                    if len(tmp) < len(r):
                        tmp = r
        return tmp


# 切割子串
def cut(s: str):
    results = []
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        for i in range(len(s) - x):
            results.append(s[i:i + x + 1])
    return results


def isPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


if __name__ == '__main__':
    str = 'abcacba'
    s = Solution()
    print(s.longestPalindrome(str))
