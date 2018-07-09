# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        in_list = {'(': 1, '[': 2, '{': 3}
        out_list = {')': 1, ']': 2, '}': 3}
        stack = []
        if s == []:
            return True
        if s in out_list or s in in_list:
            return False
        for k in s:
            if k in in_list:
                stack.append(in_list[k])
            if k in out_list:
                if out_list[k] != stack.pop(-1):
                    return False
        return True

# 范例
class Solution__:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = {')': '(', ']': '[', '}': '{'}
        l = [None]
        for i in s:
            if i in a and a[i] == l[-1]:
                l.pop()
            else:
                l.append(i)
        return len(l) == 1
