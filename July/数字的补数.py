'''
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

注意:

给定的整数保证在32位带符号整数的范围内。
你可以假定二进制数不包含前导零位。
示例 1:

输入: 5
输出: 2
解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。
示例 2:

输入: 1
输出: 0
解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。
'''


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = bin(num)[2:]
        r = ''
        for i in tmp:
            if i == '1':
                r += '0'
            else:
                r += '1'
        return int(r, 2)


# 优秀答案
class Solution__:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        p = num
        while num != 0:
            num = num // 2
            count += 1
        res = 2 ** count - 1 - p
        return res


if __name__ == '__main__':
    S = Solution()
    r = S.findComplement(2)
    print(r)
