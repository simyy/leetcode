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

1   5   9
2 4 6 8 10
3   7   11

and,

1   7     13
2 6 8  12 14
3 5 9  11 15
4   10    16



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
