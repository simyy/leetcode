/*
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

Analysis:
问题：把整数转化为罗马数字。
由于题目只给了限制，最大的为3999，那么只需要{'I','V','X','L','C','D','M'}几个字符：
I = 1;
V = 5;
X = 10;
L = 50;
C = 100;
D = 500;
M = 1000;
本体的解析思路和大数转化为字符串保存类似。
需要注意的是
1.1-3或10-30或100-300分别为I/II/III,X/XX/XXX,C/CC/CCC
2.4或40或400分别为IV,XL,CD
3.6-8或60-80或600-800分别为VI/VII/VIII，LX/LXX/LXXX,DC/DCC/DCC
4.9或90或900分别为IX,XC,CM
*/

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        char symbol[7] = {'I','V','X','L','C','D','M'};
        string roman = "";
        int t = 1000;
        int i = sizeof(symbol) - 1; 
        while (num) {
            int n = num/t;
            if (n == 9) {
                roman.append(1, symbol[i]);
                roman.append(1, symbol[i+2]);
            }
            else if ((n <=8) && (n >= 5)) {
                roman.append(1, symbol[i+1]);
                roman.append(n-5, symbol[i]);
            }
            else if (n == 4) {
                roman.append(1, symbol[i]);
                roman.append(1, symbol[i+1]);
            }
            else if ((n>0) && (n <= 3)) {
                roman.append(n, symbol[i]);
            }
            cout<<n<<"\t"<<i<<endl;

            num = num%t;
            t /= 10;
            i -= 2;

        }
        return roman;
    }
};

int main(int argc, char** argv)
{
    Solution a;

    string r = a.intToRoman(9);
    cout<<r<<endl;

    return 0;
}
