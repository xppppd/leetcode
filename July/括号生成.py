#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
import random


class Solution:
    def generateParenthesis(self, n):
        res = []
        self.generate(n, n, "", res)
        return res

    def generate(self, left, right, str, res):
        if left == 0 and right == 0:
            res.append(str)
            return
        if left > 0:
            self.generate(left - 1, right, str + '(', res)
        if right > left:
            self.generate(left, right - 1, str + ')', res)


# 括号检查
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
