# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
#
# 请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 中位数是 2.0
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 中位数是 (2 + 3)/2 = 2.5




class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        lenth = len(nums1)
        if lenth % 2 == 0:
            return (nums1[lenth // 2 - 1] + nums1[lenth // 2]) / 2
        else:
            return nums1[lenth / 2]


if __name__ == '__main__':
    l1 = [1, 3]
    l2 = [5, 7]
    s = Solution()
    print(s.findMedianSortedArrays(l1, l2))
