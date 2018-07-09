# 实现 atoi，将字符串转为整数。
#
# 在找到第一个非空字符之前，需要移除掉字符串中的空格字符。如果第一个非空字符是正号或负号，
# 选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，
# 则直接将其与之后连续的数字字符组合起来，形成整数。
#
# 字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。
#
# 当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。
#
# 若函数不能执行有效的转换，返回 0。
#
# 说明：
#
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。如果数值超过可表示的范围，
# 则返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
#

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = 0
        f = 1
        d = 0
        str = str.strip()
        if str == '':
            return result
        if str[0] == '-':
            f = -1
            d = 1
        elif str[0] == '+':
            d = 1
        for c in str[d:]:
            if c.isnumeric():
                result = int(c) + result * 10
            else:
                break
        return max(-2 ** 31, min(result * f, 2 ** 31 - 1))


# 56ms范例
class Solution___:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0: return 0
        ls = list(str.strip())

        # sign = -1 if ls[0] == '-' else 1
        if ls[0] == '-':
            sign = -1
        else:
            sign = 1
        if ls[0] in ['-', '+']: del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))


if __name__ == '__main__':
    s = Solution()
    r = s.myAtoi("42")
    print(r)
