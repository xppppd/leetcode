#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


#写了几种思路 效率都不高
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # solution = []
        # index = 0
        # n = len(nums)
        # for k in nums:
        #     target = -k
        #     dict = {}
        #     for i in range(n):
        #         if i < index and:
        #             a = target - nums[i]
        #             if nums[i] in dict:
        #                 answer = [nums[index], nums[dict[nums[i]]], nums[i]]
        #                 answer.sort()
        #                 if answer not in solution:
        #                     solution.append(answer)
        #             else:
        #                 dict[a] = i
        #     index += 1
        # return solution
        # [-4, -1, -1, 0, 1, 2,7,9,11]
        nums.sort()
        count = len(nums)
        collect = []
        for i in range(count):
            left = i + 1
            right = count - 1
            # 避免重复找同一个数据
            if i > 0 and nums[i] == nums[i - 1]:
                left += 1
                continue
            # 数据按小到大排列，每次选取nums[i]，在其后寻找符合a + b + c = 0的两个数据
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    col = [nums[i], nums[left], nums[right]]
                    collect.append(col)
                    left += 1
                    right -= 1
                    # 循环中nums[i]已确定，当再确定1个数时，另一个数也确定，左右端任一端出现重复均可跳过
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
        return collect
        # n = len(nums)
        # dict = {}
        # solution = []
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         sum = nums[i] + nums[j]
        #         dict[sum] = [(i, j)]
        # print(dict)
        #         for k in range(n):
        #             if -nums[k] in dict and k != dict[-nums[k]][0] and k != dict[-nums[k]][1]:
        #                 answer = [nums[dict[-nums[k]][0]], nums[dict[-nums[k]][1]], nums[k]]
        #                 answer.sort()
        #                 if answer not in solution:
        #                     solution.append(answer)
        # return solution

# 之前的twoSum
def twoSum(sums: list, k):
    dict = {}
    for i in range(len(sums)):
        a = k - sums[i]
        if sums[i] in dict:
            return [dict[sums[i]], i]
        else:
            dict[a] = i


if __name__ == '__main__':
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6]
    s = Solution()
    l = s.threeSum(nums)
    print(l)
