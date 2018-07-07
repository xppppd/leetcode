# 从排序数组中删除重复项
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 太慢了
        # for i in range(1, len(nums) + 1):
        #     if nums[-i] in nums[:-i]:
        #         nums.append(nums.pop(-i))
        #         count -= 1
        # return nums[:count]
        length = len(nums)
        i = 0
        j = 1
        while j < length:
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                j += 1
                i += 1
        return nums[0:i+1]


if __name__ == '__main__':
    s = Solution()
    l = [1,1,2]
    print(s.removeDuplicates(l))
