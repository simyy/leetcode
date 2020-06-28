# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-194/problems/avoid-flood-in-the-city/
"""

# Time Limit Exceeded
# class Solution(object):
#     def avoidFlood(self, rains):
#         """
#         :type rains: List[int]
#         :rtype: List[int]
#         """
#         # self.M = {}
#         self.R = []
#         if not self.recurse([], rains):
#             return []
#         print self.R
#         return self.R
#
#     # def build_key(self, fulls, rains):
#     #     return ",".join([str(_) for _ in fulls]) + '|' + ",".join([str(_) for _ in rains[1:]])
#
#     def recurse(self, fulls, rains):
#         if len(rains) == 0:
#             return True
#         rain = rains[0]
#         if rain == 0:
#             # Find Duplicate Ones In Rains After
#             # subfulls = [full for full in fulls if full in rains]
#             subfulls = [rain for rain in rains if rain in fulls]
#             if len(subfulls) > 0:
#                 for i in range(len(subfulls)):
#                     self.R.append(subfulls[i])
#
#                     # key = self.build_key(subfulls[:i] + subfulls[i+1:], rains[1:])
#                     # if key in self.M:
#                     #     r = self.M[key]
#                     # else:
#                     #     r = self.recurse(subfulls[:i] + subfulls[i+1:], rains[1:])
#                     # if r:
#                     #     return True
#
#                     if self.recurse(subfulls[:i] + subfulls[i+1:], rains[1:]):
#                         return True
#
#                     self.R.pop(-1)
#             else:
#                 self.R.append(1)
#                 return self.recurse(fulls, rains[1:])
#         else:
#             if rain in fulls:
#                 return False
#             self.R.append(-1)
#
#             # key = self.build_key(fulls + [rain], rains[1:])
#             # if key in self.M:
#             #     return self.M[key]
#             # else:
#             #     return self.recurse(fulls + [rain], rains[1:])
#
#             return self.recurse(fulls + [rain], rains[1:])


# Time Limit Exceeded
# class Solution(object):
#     def avoidFlood(self, rains):
#         """
#         :type rains: List[int]
#         :rtype: List[int]
#         """
#         r = [1] * len(rains)
#         d = {}
#         suns = []
#         for i in range(len(rains)):
#             rain = rains[i]
#             if rain == 0:
#                 suns.append(i)
#             else:
#                 if rain in d:
#                     if len(suns) > 0:
#                         for k in range(len(suns)):
#                             j = suns[k]
#                             if j > d[rain]:
#                                 r[j] = rain
#                                 suns.pop(k)
#                                 break
#                         else:
#                             return []
#                     else:
#                         return []
#                 d[rain] = i
#                 r[i] = -1
#         print r
#         return r

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        r = [1] * len(rains)
        d = {}
        suns = []
        for i in range(len(rains)):
            rain = rains[i]
            if rain == 0:
                suns.append(i)
            else:
                if rain in d:
                    if len(suns) > 0:
                        for k in range(len(suns)):
                            j = suns[k]
                            if j > d[rain]:
                                r[j] = rain
                                suns.pop(k)
                                break
                        else:
                            return []
                    else:
                        return []
                d[rain] = i
                r[i] = -1
        print r
        return r




if __name__ == '__main__':
    assert Solution().avoidFlood([1,2,3,4]) == [-1, -1, -1, -1]
    assert Solution().avoidFlood([1,2,0,0,2,1]) == [-1,-1,2,1,-1,-1]
    assert Solution().avoidFlood([1,2,0,1,2]) == []
    assert Solution().avoidFlood([69,0,0,0,69]) == [-1,69,1,1,-1]
    assert Solution().avoidFlood([10,20,20]) == []
    assert Solution().avoidFlood([1,2,0,2,3,0,1]) == [-1,-1,2,-1,-1,1,-1]
    assert Solution().avoidFlood([3,5,4,0,1,0,1,5,2,8,9]) == [-1,-1,-1,5,-1,1,-1,-1,-1,-1,-1]
    assert Solution().avoidFlood([0, 1, 1]) == []
    assert Solution().avoidFlood([1,0,2,3,0,1,2]) == [-1,1,-1,-1,2,-1,-1]
    assert Solution().avoidFlood([2,3,0,0,3,1,0,1,0,2,2]) == []