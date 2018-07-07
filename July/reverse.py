# 给定一个 32 位有符号整数，将整数中的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        f = x // abs(x)
        result = int(str(abs(x))[::-1]) * f
        if -2 ** 31 <= result <= 2 ** 31 - 1:
            return result
        else:
            return 0



#执行用时为 36 ms 的范例
class Solution__(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum = 0
        if x < 0 :
            y = -x
        else :
            y = x
        while (y>0):
            sum = sum*10 + y%10
            y = y/10

        if sum > (2**31-1) or -sum < -2**31:
            return 0
        else:
            if x < 0 :
                return -sum
            else:
                return sum

if __name__ == '__main__':
    s = Solution()
    r = s.reverse(x=-12300)
    print(r)