'''

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。
'''


# 数据太多时会超时
class Solution:
    def Jump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # def jump(nums, count, result):
        #     if len(nums) == 1:
        #         result.append(count)
        #         return
        #     if nums[0] == 0:
        #         return
        #     if nums[0] >= len(nums) - 1:
        #         result.append(count + 1)
        #         return
        #     for i in range(nums[0]):
        #         jump(nums[i + 1:], count + 1, result)
        #     return
        #
        # result = []
        # count = 0
        # jump(nums, count, result)
        # if result:
        #     return min(result)
        # else:
        #     return []
        nums.reverse()

        def jump_to(nums, count):
            if nums[0] == 0:
                return 0
            elif len(nums) == 1:
                return count
            tmp = [0]
            for index, i in enumerate(nums[1:]):
                if i > index:
                    tmp.append(index + 1)
            j = max(tmp)
            if j == len(nums) - 1:
                return count
            elif j == 0:
                return 0
            else:
                return jump_to(nums[j:], count + 1)

        return jump_to(nums, 1)


if __name__ == '__main__':
    s = Solution()
    list = [1]
    r = s.Jump(list)
    print(r)
