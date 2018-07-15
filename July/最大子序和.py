'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''


# 动态规划，记录从头开始的子串

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        max_n = max(nums)
        tmp = 0
        start = 0
        for i in range(l):
            tmp += nums[i]
            if tmp < 0:
                start = i
                tmp = 0
            else:
                max_n = max(max_n, tmp)
        return max_n


# 优秀解答
class Solution__:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        sum = 0
        for num in nums:
            sum = sum + num if sum > 0 else num
            result.append(sum)
        return max(result)
