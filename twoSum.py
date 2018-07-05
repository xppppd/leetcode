'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        k = target - nums[i]
        if k in nums[i + 1:]:
            return [i, nums[i + 1:].index(k) + i + 1]
    return None


# 他人优秀答案
def twoSum__(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 用len()方法取得nums列表长度
    n = len(nums)
    # 创建一个空字典
    d = {}
    for x in range(n):
        a = target - nums[x]
        # 字典d中存在nums[x]时
        if nums[x] in d:
            return d[nums[x]], x
        # 否则往字典增加键/值对
        else:
            d[a] = x
            # 边往字典增加键/值对，边与nums[x]进行对比
