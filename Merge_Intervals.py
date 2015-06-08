/*
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]

Analysis:
there are three situations, such as

1.   |_____|
  |_____|
  
2.  |_____|
  |_________|
  
3. |____|
           |_____|
           
*/

#!/usr/bin/env python
# encoding=utf-8

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        i = 1 
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
        Interval(2,6),
        Interval(8,10),
        Interval(15,18),
        ]
    a = Solution()
    result = a.merge(param)

    for item in result:
        print item.start, item.end
