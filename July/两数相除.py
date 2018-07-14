'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
'''


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0
        if dividend > 0 and divisor > 0:
            flag = 1
        elif dividend < 0 and divisor < 0:
            flag = 1
        else:
            flag = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        i = 31
        while i >= 0:
            if divisor << i <= dividend:
                dividend -= divisor << i
                result += 1 << i
            else:
                i -= 1
        # if i == 0:
        #     result += 1
        if not flag:
            result = -result
        if result < -2 ** 31:
            result = 2 ** 31
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        return result


# 优秀答案 利用 range(x,y,x)取长度
class Solution__:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        sign = 1 if (dividend < 0) == (divisor < 0) else -1

        x, y = abs(dividend), abs(divisor)

        if x < y:
            return 0

        if x == y:
            return sign

        arange = range(y, x, y)
        alen = len(arange)
        if arange[-1] + y <= x:
            alen += 1

        if sign == -1:
            alen = -alen
        return min(alen, 2 ** 31 - 1)


if __name__ == '__main__':
    s = Solution()
    r = s.divide(dividend=10, divisor=3)
    print(r)
