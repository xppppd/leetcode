class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        answer = []
        result = []
        # if target in candidates:
        #     result.append([target])
        self.compute(candidates, target, 0, answer, result)
        return result

    def compute(self, candidates, target, start, answer, result):
        for i in range(start, len(candidates)):
            if target > 0:
                answer.append(candidates[i])
                self.compute(candidates, target - candidates[i], i + 1, answer, result)
                answer.pop()
            elif target < 0:
                return
        if target == 0:
            temp = answer[:]
            if temp not in result:
                result.append(temp)
            return


if __name__ == '__main__':
    s = Solution()
    candidates = [1, 1,2]
    r = s.combinationSum2(candidates, 2)
    print(r)
