'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
'''


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target in nums:
            return nums.index(target)
        else:
            return self.searchInsert(nums, target + 1)

# 优秀解答
class Solution__:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target in nums:
            return nums.index(target)
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (j - i) // 2 + i
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return i if nums[i] > target else i + 1