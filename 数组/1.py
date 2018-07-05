# 从排序数组中删除重复项
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        for i in range(1, len(nums) + 1):
            if nums[-i] in nums[:-i]:
                nums.append(nums.pop(-i))
                count -= 1
                print(nums)
        return nums[:count]


if __name__ == '__main__':
    s = Solution()
    l = [1, 2, 3, 3, 4, 5, 5, 7, 3, 3, 3, 2, 8, 5, 4, 7]
    print(s.removeDuplicates(l))
