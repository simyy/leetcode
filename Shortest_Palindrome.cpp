
//Time Limit Exceeded
class Solution {
public:
    string shortestPalindrome(string s) {
        string tmp = s;
        int len = s.size();
        if (len <= 1)
            return s;
        for (int i = 0; i < len; ++i) {
            s.insert(i, tmp.substr(len-i-1, 1));
            if (isPalindrome(s, i) == true)
                return s;
        }
    }
    
    bool isPalindrome(string str, int i)
    {
        int l = 0 + i;
        int r = str.size() - 1 - i;
        while (l < r) {
            if (str[l++] != str[r--])
                return false;
        }
        return true;
    }
};
