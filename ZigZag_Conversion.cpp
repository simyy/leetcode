/*
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

how to understand this solution?

example as:

0   4   8
1 4 5 7 9
2   6   10

and,

0     6       12
1   5 7    11 13
2 4   8  10   14
3     9       15

1.由此可以发现如果把中间缺少数字的部分去掉的话，可以发现行与行之间的差值为n*(2*rows-2)，例如0 + 2 * 4 - 2 = 6, 6 + 2 * 4 -2 = 12
2.注意中间缺少数字的部分，如果是第一行和最后一行需要跳过
2.再看缺少数字部分的规律，由于7 = 1 + 2*rows - 2，那么5呢？而8 = 2 + 2*rows - 2,那么4呢？
  根据规律可以发现，5 = 7 - 2 * 1， 4 = 8 - 2 * 2，那么，中间的数字可以归纳为，num = n*(2*rows-2-2*i)
*/


#include <iostream>
#include <string.h>

using namespace std;

class Solution {

public:

    string convert(string s, int nRows) {
        int len = s.size();

        if (len < 3 || nRows < 2 || len <= nRows) return s;  

        int interval = 2*nRows - 2;

        string res = "";

        for (int i = 0; i < nRows; ++i) {
            for (int j = i; j < len; j += interval) {
                res += s[j];
                
                if ((i > 0) && (i < nRows-1)) {
                    int special_interval = interval - 2 * i;
                    if (j + special_interval < len)
                        res += s[j + special_interval];
                }
            }
        }

        return res;
    }

};


int main(int args, char** argc)
{
    Solution a;

    //string s = a.convert("PAYPALISHIRING", 3);
    string s = a.convert("ABCD", 3);

    cout<<s<<endl;

    return 0;
}
