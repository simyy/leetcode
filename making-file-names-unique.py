# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-194/problems/making-file-names-unique/
"""

class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        res = []
        d = {}
        for name in names:
            if name in d:
                # 单调递增
                k = d[name] + 1
                while (name + '(%d)' % k) in d:
                    k += 1
                d[name] = k
                name = name + '(%d)' % k
            d[name] = 0
            res.append(name)
        return res



if __name__ == '__main__':
    assert Solution().getFolderNames(["pes","fifa","gta","pes(2019)"]) == ["pes","fifa","gta","pes(2019)"]
    assert Solution().getFolderNames(["gta","gta(1)","gta","avalon"]) == ["gta","gta(1)","gta(2)","avalon"]
    assert Solution().getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]) == ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
    assert Solution().getFolderNames(["wano","wano","wano","wano"]) == ["wano","wano(1)","wano(2)","wano(3)"]
    assert Solution().getFolderNames(["kaido","kaido(1)","kaido","kaido(1)"]) == ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
    assert Solution().getFolderNames(["v(1)","r","k","e","h(3)","t","b(1)","s(4)","n(1)(4)","u(2)(4)","c(1)","v(4)(4)","f","m","y","w","p","n","j","i","z","b","h","r","w","j","i","h(4)","f","u(1)","c","k","t(2)(4)","m","o(3)","s","e","m(3)(4)","q","h(1)(3)","f","w","t","w","u(1)(2)","j","k","k","n","a","b","v"]) \
         == ["v(1)","r","k","e","h(3)","t","b(1)","s(4)","n(1)(4)","u(2)(4)","c(1)","v(4)(4)","f","m","y","w","p","n","j","i","z","b","h","r(1)","w(1)","j(1)","i(1)","h(4)","f(1)","u(1)","c","k(1)","t(2)(4)","m(1)","o(3)","s","e(1)","m(3)(4)","q","h(1)(3)","f(2)","w(2)","t(1)","w(3)","u(1)(2)","j(2)","k(2)","k(3)","n(1)","a","b(2)","v"]