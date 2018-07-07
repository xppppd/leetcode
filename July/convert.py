# 将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"
#
# 实现一个将字符串进行指定行数变换的函数:
#
# string convert(string s, int numRows);
# 示例 1:
#
# 输入: s = "PAYPALISHIRING", numRows = 3
# 输出: "PAHNAPLSIIGYIR"
# 示例 2:
#
# 输入: s = "PAYPALISHIRING", numRows = 4
# 输出: "PINALSIGYAHRPI"
# 解释:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # (s - 1)的倍数
        # s*n号 位于 sn-1 处
        #
        pass


def con(s, numRows):
    l = [[]]
    d = []
    for i in range(s):
        l.append([''])
    length = len(numRows)
    for i in range(length):
        if i % (2 * s - 1) >= 4:
            d.append(-1)
        else:
            d.append(1)
    for i in range(length):
        j = -1
        l[j + d[i]] += numRows[i]
    return l
    # for i in range(length):
    #     if length // s


if __name__ == '__main__':
    l = con(4, 'PAHNAPLSIIGYIR')
    print(l)
