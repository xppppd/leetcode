'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''


class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        answer = []
        result = []
        self.compute(candidates, target, 0, answer, result)
        return result

    def compute(self, candidates, target, start, answer, result):
        for i in range(start, len(candidates)):
            if target > 0:
                answer.append(candidates[i])
                self.compute(candidates, target - candidates[i], i, answer, result)
                answer.pop()
            elif target < 0:
                return
            else:
                temp = answer[:]
                result.append(temp)
                return


if __name__ == '__main__':
    s = Solution()
    candi = [2, 3, 5]
    tar = 8
    r = s.combinationSum(candi, tar)
    print(r)
