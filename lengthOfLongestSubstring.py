# 给定一个字符串，找出不含有重复字符的最长子串的长度。
#
# 示例：
#
# 给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
#
# 给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = ''
        tmp = ''
        for i in s:
            if i in tmp:
                tmp = tmp[tmp.index(i) + 1:] + i
            else:
                tmp += i
                if len(record) < len(tmp):
                    record = tmp
        return len(record)


if __name__ == '__main__':
    str = ""
    s = Solution()
    print(s.lengthOfLongestSubstring(str))
