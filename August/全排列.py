import itertools

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in itertools.permutations(nums):
            result.append(i)
        return result



