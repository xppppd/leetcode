# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
class Solution:
    def trap(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        top_index = 0
        length = len(h)
        left = 0
        right = length - 1
        rain = 0
        move_top = 0
        if length < 3:
            return rain
        #先找出最高的柱子
        for i in range(length):
            if h[i] > h[top_index]:
                top_index = i
        # 分别从两端遍历，用移动中的最高值move_top减去当前值得到rain
        while left < top_index:
            if h[left] > move_top:
                move_top = h[left]
            rain += move_top - h[left]
            left += 1
        move_top = 0
        while right > top_index:
            if h[right] > move_top:
                move_top = h[right]
            rain += move_top - h[right]
            right -= 1
        return rain


if __name__ == '__main__':
    s = Solution()
    height = [5,2,1,2,1,5]
    r = s.trap(height)
    print(r)
