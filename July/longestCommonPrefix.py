#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        if strs == []:
            return result
        strs.sort()
        #取排序后的第一个跟最后一个查找公共部分
        f = min(len(strs[-1]), len(strs[0]))
        for i in range(f):
            if strs[0][i] == strs[-1][i]:
                result += strs[0][i]
            else:
                return result
        return result



#执行用时为 24 ms 的范例
class Solution___(object):
    def longestCommonPrefix(self, strs):
        """
    :type strs: list[str]
    :rtype: str
    """

        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for item in strs[1:]:
            while item.find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix

if __name__ == '__main__':
    s = Solution()
    strs = []
    r = s.longestCommonPrefix(strs)
    print(r)
