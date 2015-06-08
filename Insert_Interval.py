/*
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

*/

#!/usr/bin/env python
# encoding=utf-8

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        i = 1 
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x:x.start)
        while i < len(intervals):
            if intervals[i].start <= intervals[i - 1].end and intervals[i].end >= intervals[i - 1].end:
                intervals[i-1].end = intervals[i].end
                intervals.pop(i)
            elif intervals[i].start <= intervals[i - 1].end and intervals[i].end <= intervals[i - 1].end:
                intervals.pop(i)
            else:
                i += 1
        return intervals


if __name__ == "__main__":
    param = [
        Interval(1,3),
        Interval(6,9),
        ]
    a = Solution()
    result = a.insert(param, Interval(2,5))

    for item in result:
        print item.start, item.end
