# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。画 n 条垂直线，
# 使得垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 注意：你不能倾斜容器，n 至少是2。


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)
        max_area = 0
        while left < right:
            area = (right - left -1) * min(height[left], height[right - 1])
            if area > max_area:
                max_area = area
                solution = (left, right)
            if height[left] < height[right - 1]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    height = [1, 2, 3, 2, 2]
    s = Solution()
    print(s.maxArea(height))
