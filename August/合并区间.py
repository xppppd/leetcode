'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # intervals.sort(key = lambda startone:startone.start)
        # result = []
        # left = 0
        # right = 0
        # for interval in intervals:
        #     if interval.start >= right:
        #         left = interval.start
        #         right = interval.end
        #         i = intervals.index(interval)
        #         for interval in intervals[i:]:
        #             if interval.start <= right:
        #                 right = interval.end
        #         result.append(Interval(left,right))
        # return result
        length = len(intervals)
        if length < 2:
            return intervals
        intervals.sort(key=lambda startone: startone.start)
        result = []
        #已排序后的区间只用考虑start，end是否大于当前区间end，
        flag = 1
        now = Interval(0,0)
        for interval in intervals:
            if flag == 1:
                now = interval
                flag = 0
                continue
            if interval.start > now.end:
                result.append(now)
                now = interval
            elif interval.end <= now.end:
                continue
            else:
                now.end = interval.end
        result.append(now)
        return result




