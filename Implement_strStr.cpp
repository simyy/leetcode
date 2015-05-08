/*
Implement strStr().
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
*/

class Solution {
public:
    int strStr(string haystack, string needle) {
        int len_haystack = haystack.size();
        int len_needle = needle.size();
        if (len_needle > len_haystack)
            return -1;
        if (len_needle == 0)
            return 0;
        for (int i = 0; i <= len_haystack-len_needle; ++i) {
            for (int j = 0; j < len_needle; ++j) {
                if (haystack[j+i] == needle[j])
                    if (j == len_needle - 1)
                        return i;
                    else
                        continue;
                else
                    break;
            }
            
        }
        return -1;
    }
};
